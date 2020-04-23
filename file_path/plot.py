import os
import matplotlib.pyplot as plt
import numpy as np

# #这是一组使用：
# x = np.arange(0, 100)
# #划分子图
# fig,axes=plt.subplots(2,2)
# ax1=axes[0,0]
# ax2=axes[0,1]
# ax3=axes[1,0]
# ax4=axes[1,1]
# #作图1
# ax1.plot(x, x)
# #作图2
# ax2.plot(x, -x)
# #作图3
# ax3.plot(x, x ** 2)
# ax3.grid(color='r', linestyle='--', linewidth=1,alpha=0.3)
# #作图4
# ax4.plot(x, np.log(x))
# plt.show()


# #这是一组使用，由上面改过来，注意更改成一行两列以后子图的索引要成为一维
# x = np.arange(0, 100)
# #划分子图
# fig,axes=plt.subplots(1,2)
# ax1=axes[0]
# ax2=axes[1]
# # ax3=axes[1,0]
# # ax4=axes[1,1]
# #作图1
# ax1.plot(x, x)
# #作图2
# ax2.plot(x, -x)
# #作图3
# # ax3.plot(x, x ** 2)
# # ax3.grid(color='r', linestyle='--', linewidth=1,alpha=0.3)
# # #作图4
# # ax4.plot(x, np.log(x))
# plt.show()


#下面是另一组
x = np.arange(0, 100)
#作图1
plt.subplot(221)
plt.plot(x, x)
#作图2
plt.subplot(222)
plt.plot(x, -x)
#作图3
plt.subplot(223)
plt.plot(x, x ** 2)
plt.grid(color='r', linestyle='--', linewidth=1,alpha=0.3)
# #作图4  这里不注释掉会出现分母存在为零的情况的报错
# plt.subplot(224)
# plt.plot(x, np.log(x))
plt.show()



# def log_data():
#
#     accuracyList=[]
#     with open((os.path.join('./txt_file/self-unet-way.txt')), 'r') as f:
#         data = f.read()
#     # if data.index()%2==0:
#     strlist = data.split('loss: ')
#     for item in strlist[1:]:
#         try:
#             accuracy = item.split(' - accuracy:')[0]
#             print(accuracy)
#             accuracyList.append(accuracyList,accuracy)
#
#         except:
#             pass
#     # for  acc in accuracyList:
#     #     plt.plot(acc)
#
#     # x = np.arange(0, 100)
#     # plt.plot(x,accuracyList[x])
#
#
# # main运行
# if __name__ == '__main__':
#     log_data()