import glob
from ipdb import set_trace as bp
from random import shuffle
import shutil
import os

# bp()
for i in range(660):
    temp = ("qdata/test/{}".format(i)) 
#     bp()
    os.mkdir(temp)

for i in range(660):
    list = glob.glob("qdata/train/{}/*.png".format(i))
#     bp()
#     print(list)
    shuffle(list)
    for i in range(int(len(list)*0.1)):
        # print()
        # break
        source = list[i]
        destinate = list[i].replace("train","test")
        shutil.move(source, destinate)
#     break
        # print(i)

#     print(list)
#     break
#     if len(list)>2500:
        # print(i," ",len(list))
