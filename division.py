from PIL import Image
import numpy as np
from tqdm import tqdm
from ipdb import set_trace as bp
from torchvision import transforms
import os
import glob

print(">>> Hello world <<<")
transformation = transforms.Compose([transforms.Resize((64,64))])
wordlist = {}
f = open("myconstant.txt" , "r", encoding= "utf-8")
lines = f.readlines()
for line in lines:
    line.replace("\n","")
    wordlist[line[0]] = int(line.split(" ")[1].replace("\n",""))
    # print(int(line.split(" ")[1].replace("\n","")))
f = open("eval/temp3.txt", "r", encoding="utf-8")
lines = f.readlines()
temp = ""
for line in lines:
    label = line.split("|")[1]
    label.replace("\n","")
    for c in label:
        xx = c.replace("\n","")
        if xx not in wordlist:
            temp = temp + xx
            # print(1)
            # pass
            # print(c)
print(temp)
# print(wordlist)
# f = open("eval/label.txt", "r", encoding="utf-8")
# lines = f.readlines()
# dem = 0
# id = -1
# for line in tqdm(lines):
# total_count = 0
# for line in lines:
#     id += 1
#     # print(line.split("|")[0])
#     img = Image.open("eval/" + line.split("|")[0])
#     np_img = np.array(img)
#     # print(np_img.shape)
#     height, width = np_img.shape[0], np_img.shape[1]
#     temp_img = np.zeros([height, width, 3], dtype=np.uint8)

#     real_img = np.zeros([height, width, 3], dtype=np.uint8)

#     temp_img[:, :, 0] = np_img
#     temp_img[:, :, 1] = np_img
#     temp_img[:, :, 2] = np_img

#     real_img[:, :, 0] = np_img
#     real_img[:, :, 1] = np_img
#     real_img[:, :, 2] = np_img
    
#     for i in range(height):
#         for j in range(width):
#             if temp_img[i, j, 0] < 200:
#                 temp_img[i, j, 0] = 0
#                 temp_img[i, j, 1] = 0
#                 temp_img[i, j, 2] = 0
#             else:
#                 temp_img[i, j, 0] = 255
#                 temp_img[i, j, 1] = 255
#                 temp_img[i, j, 2] = 255

#     left = 0
#     for j in range(5, width):
#         flag = False
#         for i in range(height):
#             if temp_img[i, j, 0] == 0:
#                 flag = True

#         if flag == True:
#             left = j
#             break

#     right = width-1
#     for j in range(width-1, 0, -1):
#         flag = False
#         for i in range(height):
#             if temp_img[i, j, 0] == 0:
#                 flag = True
#         if flag == True:
#             right = j
#             break

#    # print(left," ",right)
#     temp_cot = []
#     for j in range(left+10, right-10):
#         flag = False
#         for i in range(height):
#             if temp_img[i, j, 0] == 0:
#                 flag = True

#         if flag == False:
#             temp_cot.append(j)
#             for i in range(height):
#                 temp_img[i, j, 0] = 255
#                 temp_img[i, j, 1] = 0
#                 temp_img[i, j, 2] = 0
    
#     fear = 0
#     for i in range(len(temp_cot)-1):
#         if (temp_cot[i+1]-temp_cot[i])>1:
#             fear += 1
#     # print(temp_cot)
#     # img = Image.fromarray(temp_img)
#     temp_string = str(id)+".png"
#     if len(line.split("|")[1].replace("\n",""))==(fear+2):
        
#         idx = 0
#         cc = 0
#         rr_cot = []
#         # rr_cot.append(0)
#         temp_cot.append(width)
#         # print(temp_cot)
#         for ll in range(1,len(temp_cot)):
#             if abs(temp_cot[ll]-temp_cot[ll-1])==1:
#                 idx += temp_cot[ll]
#                 cc += 1

#             else:
#                 idx=int(idx/cc)
#                 rr_cot.append(idx)
#                 idx = 0
#                 cc = 0
#         # print(rr_cot)
#         # rr_cot.append(width)
#         for tt in rr_cot:
#             for x in range(height):
#                 real_img[x, tt, 0] = 255
#                 real_img[x, tt, 1] = 0
#                 real_img[x, tt, 2] = 0
#         rr_cot.insert(0,0)
#         rr_cot.append(width)
#         img = Image.fromarray(real_img)
#         label = line.split("|")[1].replace("\n","")
#         ddd = 0
#         # tt_img
#         # bp()
#         link_data = "data/test/"
#         for ii in range(len(label)):
#             tt_img = real_img[:,rr_cot[ii]:rr_cot[ii+1],:]
#             tt_img = Image.fromarray(tt_img)
#             tt_img = transformation(tt_img)
#             lala = str(wordlist[label[ii]])
#             if os.path.isdir(link_data + lala)==False:
#                 os.mkdir(link_data + lala)
#             list_img = len(glob.glob(link_data + lala+"/*.*"))
#             tt_img.save(link_data + lala + "/" + str(list_img)+".png")
#             # ddd += 2 
#             # print(label[ii])
#         # bp()
#         # break```
#     #     total_count +=1
#         img.save(str(id)+"_"+str(fear)+".png")
# #    print(temp_string," ",line.split("|")[1].replace("\n",""))
# #    img.save(str(id)+"_"+str(len(line.split("|")[1].replace("\n","")))+".png")

# print(total_count)
# print(">>> done <<<")
#    bp()
#    img.show()
#    mystr = input()
#    if mystr.find("y") != "-1":
#        img.save(str(id)+".png")
