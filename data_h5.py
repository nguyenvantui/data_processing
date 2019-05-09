import csv
import os
import numpy as np
import h5py
import glob
from PIL import Image
from ipdb import set_trace as bp
from tqdm import tqdm

datapath = "data.h5"
# bp()
train_link = "data/train/_/*.png"
test_link = "data/test/_/*.png"
train_list = []
train_label = []
test_list = []
test_label = []
total_num = 659
for x in tqdm(range(total_num)):

#     print(x)
    link = train_link.replace("_", str(x))
    # print(link)
    list = glob.glob(link)

    for file in list:
        # print(file)
        im = Image.open(file)
        im = np.array(im)
        im = im[:,:,0]
        # bp()
        # im = 255 - np.array(im)
        train_list.append(im.tolist())
        train_label.append(x)
        # img = im.tolist()

print("=============")
print(">>> Fast <<<")

for x in tqdm(range(total_num)):
    link = test_link.replace("_", str(x))
    list = glob.glob(link)
    for file in list:
        im = Image.open(file)
        im = np.array(im)
        im = im[:,:,0]
        # im = 255 - np.array(im)
        test_list.append(im.tolist())
        test_label.append(x)

print(np.shape(train_list))
print(np.shape(test_list))
datafile = h5py.File(datapath, 'w')
datafile.create_dataset("training_pixel", dtype = 'uint8', data=train_list)
datafile.create_dataset("training_label", dtype = 'int64', data=train_label)
datafile.create_dataset("testing_pixel", dtype = 'uint8', data=test_list)
datafile.create_dataset("testing_label", dtype = 'int64', data=test_label)
datafile.close()
print(">>> done <<<")
