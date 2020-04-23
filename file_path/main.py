import os

import cv2
import numpy as np


#下面这个的DS_Store不知道怎么回事去不了
# def file_name(file_dir):
#     all_files=[]
#     for root, dirs, files in os.walk(file_dir):
#         # print("root:",root) #当前目录路径
#         # print("dirs:",dirs) #当前路径下所有子目录
#         print("files:",files) #当前路径下所有非目录子文件
#         # print(files[0])
#         # if files[0]=="DS_Store":
#         #     files.remove('DS_Store')
#         # all_files=all_files+files
#
#         # files.remove(files[0])
#
#     print("all_files:",all_files)


#下面的这个是正式使用版本，但是打印是在循环中的，正式使用要注释掉
# def listdir(path, list_name):
#     for file in os.listdir(path):
#         file_path = os.path.join(path, file)
#         if os.path.isdir(file_path):
#             listdir(file_path, list_name)
#         elif os.path.splitext(file_path)[1]=='.jpg':
#             list_name.append(file_path)
#     print("list_name:",list_name)
from PIL import Image

#下面这个在测试读取文件以及reshape调整文件大小的问题，同时发现了yeild是个函数
def unetkeras(pathX, pathY):
    print("in")
    BATCH_SIZE = 1
    # pathX = '/home/wly/Documents/file_path/train'  # change your file path
    # pathY = '/home/wly/Documents/file_path/train'  # change your file path
    print("data processing")
    # data processing
    # generator(pathX,pathY,BATCH_SIZE)
    PIXEL = 512  # set your image size
    X_CHANNEL = 3  # training data channel
    Y_CHANNEL = 3  # test data channel
    # while 1:
    X_train_files = []
    Y_train_files = []
    X_train_files = listdir(pathX, X_train_files)
    Y_train_files = listdir(pathY, Y_train_files)
    print("X_train_files",X_train_files)
    X_NUM = len(X_train_files)
    Y_NUM = len(Y_train_files)
    print("X_NUM:", X_NUM)
    print("Y_NUM:", Y_NUM)
    # add up
    a = (np.arange(1, X_NUM))

    X = []
    Y = []
    for i in range(BATCH_SIZE):
        index = np.random.choice(a)
        # ipdb.set_trace()
        img = cv2.imread(  X_train_files[index], 1)

        print("imgx path:",X_train_files[index])
        print("imgx size:",img.size) # 像素总数目
        print("imgx shape:",img.shape)  # (h,w,c)
        # print(img.dtype)
        # print(img)
            # cv2.namedWindow("Image")
            # cv2.imshow("Image", img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
                # img = Image.open(X_train_files[index])
                # print(img.mode)
        img = np.array(img).reshape(PIXEL, PIXEL, X_CHANNEL)
        print("imgx reshape path:",X_train_files[index])
        print("imgx reshape size:",img.size)
        print("imgx reshape shape",img.shape)  # (h,w,c)
        X.append(img)

        img1 = cv2.imread(Y_train_files[index], 1)
        img1 = np.array(img1).reshape(PIXEL, PIXEL, Y_CHANNEL)
        Y.append(img1)

    X = np.array(X)
    Y = np.array(Y)
    print("X shape:",X.shape)
    print("Y shape:",Y.shape)
    # yield X, Y


def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        elif os.path.splitext(file_path)[1] == '.jpg':
            list_name.append(file_path)
    # print("list_name:", list_name)
    return list_name
    # print("train datasets number:",len(list_name))


if __name__ == '__main__':
    # all_files=[]
    # listdir("train",all_files)

    print("test_unet_keras()")
    pathX = 'train'  # change your file path
    pathY = '/home/wly/Documents/file_path/train'  # change your file path
    unetkeras(pathX, pathY)
    print("out")

    # all_files = []
    # all_files = listdir(pathX, all_files)
    # print("all_files:", all_files)

    #local change
