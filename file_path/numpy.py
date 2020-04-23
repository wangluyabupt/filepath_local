import os





# X_NUM=100
# a = (numpy.arange(1, X_NUM))
# print(a)

modelpath = '/home/wly/Documents/unet-keras/checkpoints/pr/'
filepath = os.path.join(modelpath,'epoch-{epoch:02d}-{loss:.4f}.h5')
print(filepath)