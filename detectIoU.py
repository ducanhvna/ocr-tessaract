##########
# Overview
#   Bài toán đặt ra là từ một tập format có sẵn gọi là meta format chúng ta cần biết là
#   Text dó thược block nào. như vậy trước tiên chúng ta cần xác định vị trí của một text block
# Meta Format
#   Meta format là thông tin lưu trữ cấu trúc của một văn bản, bao gồm thông về kích thước chiều dài,
#   Chiều rông, thông tin về format id, thông tin cấu trúc của văn bản đó trước tiên ta xác định 
#   được 1 block array từ một văn bản. Như vậy chúng ta có định như sau
# [
#   {
#       formatid: 1,
#       width : 1024,
#       heigh: 800
#       Blockes: [
#           {
#               x: 50,
#               y: 50, 
#               width = 50,
#                heigh = 100
#             }

#         ]


#   }
# ]

# ——— Cắt text block 
# — Dầu vào format , ảnh
# B1 Load format id
# B2 detect block trong ảnh
# B3 duyệt tất cả cac block trong meta format
#           Tìm block nào có IoU cao nhất trong các block ảnh
#            Vẽ block đó
           
# —  Tìm meta format
# Duyệt tất cả metaforma
#      Cắt textblok
#      Tính Độ chính xác của phương pháp
##########

import json 
import cv2
import re
import pytesseract
from pytesseract import Output

def bb_intersection_over_union(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    # compute the area of intersection rectangle
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)
    # return the intersection over union value
    return iou


# Load the meta format
# Load file mata-format.json
with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data['blocks']:
        print('Width: ' + str(p['width']))
        print('Height: ' + str(p['height']))
        print('left: ' + str(p['left']))
        print('top: ' + str(p['top']))

# Load Image
img = cv2.imread('image.jpg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
# Add width heigh to size
height, width, channels = img.shape
# use tessaract detect image
dx = width/data['width']
dy = height/data['height']
print('dx: ' + str(dx))
print('dy: ' + str(dy))

# B3 duyệt tất cả cac block trong meta format
#           Tìm block nào có IoU cao nhất trong các block ảnh
#            Vẽ block đó


n_boxes = len(d['level'])
print ('level: ',n_boxes)
######### Solution 1: vùng đc chọn là vùng có iou to nhất
# for p in data['blocks']:
#     boxA = [p['left'], p['top'], p['left'] + p['width'], p['top'] + p['height'] ]

#     index = -1
#     maxvalue = 0

#     for i in range(n_boxes):
#         x0 = d['left'][i] / dx
#         y0 = d['top'][i] / dy
#         x1 = (d['left'][i] + d['width'][i]) / dx
#         y1 = (d['top'][i] + d['height'][i]) / dy

#         boxB = [x0, y0, x1, y1]
        
#         iou = bb_intersection_over_union(boxA, boxB)
#         if iou > maxvalue:
#             index = i
#             maxvalue = iou
#     if index > -1 :
#         # print(d['level'][i])
#         (x, y, w, h) = (d['left'][index], d['top'][index], d['width'][index], d['height'][index])
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

##### Solution2 trong tất cả các vùng có iou >0 thì xét
##### Buoc 1: Tim ra thanh phan nao to nhat
# for p in data['blocks']:
#     boxA = [p['left'], p['top'], p['left'] + p['width'], p['top'] + p['height'] ]

#     index = -1
#     maxvalue = 0
#     avaiablelist = []
#     for i in range(n_boxes):
#         x0 = d['left'][i] / dx
#         y0 = d['top'][i] / dy
#         x1 = (d['left'][i] + d['width'][i]) / dx
#         y1 = (d['top'][i] + d['height'][i]) / dy

#         boxB = [x0, y0, x1, y1]
        
#         iou = bb_intersection_over_union(boxA, boxB)
#         if iou >0: 
#             avaiablelist.append(i)
#         if iou > maxvalue:
            
#             index = i
#             maxvalue = iou
#     if index > -1 :
#         # print(d['level'][i])
#         (x, y, w, h) = (d['left'][index], d['top'][index], d['width'][index], d['height'][index])

#         for i in avaiablelist:
#             x0 = min(d['left'][i] / dx, x/dx)
#             y0 = min(d['top'][i] / dy, y/dy)
#             x1 = max((d['left'][i] + d['width'][i]) / dx, (x+w)/dx)
#             y1 = max((d['top'][i] + d['height'][i]) / dy, (y+h)/dy)

#             boxB = [x0, y0, x1, y1]
        
#             iou = bb_intersection_over_union(boxA, boxB)
#             if iou > maxvalue:
#                 x = int(x0)
#                 y = int(y0)
#                 w = int(x1 - x0)
#                 h = int(y1 - y0)
#                 maxvalue = iou    
#         print(x)
#         print(y)
#         print(w)
#         print(h)
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

#### Solution 3 Merge tung phia 1
# for p in data['blocks']:
#     boxA = [p['left'], p['top'], p['left'] + p['width'], p['top'] + p['height'] ]

#     index = -1
#     maxvalue = 0
#     avaiablelist = []
#     for i in range(n_boxes):
#         x0 = d['left'][i] / dx
#         y0 = d['top'][i] / dy
#         x1 = (d['left'][i] + d['width'][i]) / dx
#         y1 = (d['top'][i] + d['height'][i]) / dy

#         boxB = [x0, y0, x1, y1]
        
#         iou = bb_intersection_over_union(boxA, boxB)
#         if iou >0: 
#             avaiablelist.append(i)
#         if iou > maxvalue:
            
#             index = i
#             maxvalue = iou
#     if index > -1 :
#         # print(d['level'][i])
#         (x, y, w, h) = (d['left'][index], d['top'][index], d['width'][index], d['height'][index])

#         for i in avaiablelist:
#             x0 = d['left'][i] / dx
#             y0 = min(d['top'][i] / dy, y/dy)
#             x1 = (d['left'][i] + d['width'][i]) / dx
#             y1 = max((d['top'][i] + d['height'][i]) / dy, (y+h)/dy)

#             boxB = [x0, y0, x1, y1]
        
#             iou = bb_intersection_over_union(boxA, boxB)
#             if iou > maxvalue:
#                 x = int(x0)
#                 y = int(y0)
#                 w = int(x1 - x0)
#                 h = int(y1 - y0)
#                 maxvalue = iou 

#             ############
#             x0 = min(d['left'][i] / dx, x/dx)
#             y0 = d['top'][i] / dy
#             x1 = max((d['left'][i] + d['width'][i]) / dx, (x+w)/dx)
#             y1 = (d['top'][i] + d['height'][i]) / dy

#             boxB = [x0, y0, x1, y1]
        
#             iou = bb_intersection_over_union(boxA, boxB)
#             if iou > maxvalue:
#                 x = int(x0)
#                 y = int(y0)
#                 w = int(x1 - x0)
#                 h = int(y1 - y0)
#                 maxvalue = iou    
        
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

##### Solution 4: vet can
# from itertools import combinations 
  
# # Get all combinations of [1, 2, 3] 
# # and length 2 
# comb = combinations([1, 2, 3], 2) 
  
# # Print the obtained combinations 
# for i in list(comb): 
#     print (i)

# for p in data['blocks']:
#     boxA = [p['left'], p['top'], p['left'] + p['width'], p['top'] + p['height'] ]

#     index = -1
#     maxvalue = 0
#     avaiablelist = []
#     for i in range(n_boxes):
#         x0 = d['left'][i] / dx
#         y0 = d['top'][i] / dy
#         x1 = (d['left'][i] + d['width'][i]) / dx
#         y1 = (d['top'][i] + d['height'][i]) / dy

#         boxB = [x0, y0, x1, y1]
        
#         iou = bb_intersection_over_union(boxA, boxB)
#         if iou > 0: 
#             avaiablelist.append(i)
#     comb = combinations(avaiablelist, min(len(avaiablelist) ,3) ) 
#     (x,y,w,h)=(0,0,0,0)

#     # Print the obtained combinations 
#     for pi in list(comb): 
#         print (pi)
#         listx0 = []
#         listy0 = []
#         listx1 = []
#         listy1 = []

#         for i in pi:
#             listx0.append(d['left'][i] / dx)
#             listy0.append(d['top'][i] / dy)
#             listx1.append((d['left'][i] + d['width'][i]) / dx)
#             listy1.append((d['top'][i] + d['height'][i]) / dy)
        
        
        
#         x0 = min(listx0)
#         y0 = min(listy0)
#         x1 = max(listx1)
#         y1 = max(listy1)

#         boxB = [x0, y0, x1, y1]
        
#         iou = bb_intersection_over_union(boxA, boxB)
#         if iou > maxvalue:
#             maxvalue = iou
#             x = int(x0)
#             y = int(y0)
#             xn = int(x1)
#             yn = int(y1)
    
#     cv2.rectangle(img, (x, y), (xn, yn), (0, 255, 0), 2)
##### Solution 5: vet can lan luot
from itertools import combinations 
  
# Get all combinations of [1, 2, 3] 
# and length 2 
comb = combinations([1, 2, 3], 2) 
  
# Print the obtained combinations 
for i in list(comb): 
    print (i)

for p in data['blocks']:
    boxA = [p['left'], p['top'], p['left'] + p['width'], p['top'] + p['height'] ]

    index = -1
    maxvalue = 0
#     for i in range(n_boxes):
#         x0 = d['left'][i] / dx
#         y0 = d['top'][i] / dy
#         x1 = (d['left'][i] + d['width'][i]) / dx
#         y1 = (d['top'][i] + d['height'][i]) / dy

#         boxB = [x0, y0, x1, y1]
        
#         iou = bb_intersection_over_union(boxA, boxB)
#         if iou > maxvalue:
#             index = i
#             maxvalue = iou
#     if index > -1 :
#         # print(d['level'][i])
#         (x, y, w, h) = (d['left'][index], d['top'][index], d['width'][index], d['height'][index])
#

    avaiablelist = []
    for i in range(n_boxes):
        x0 = d['left'][i] / dx
        y0 = d['top'][i] / dy
        x1 = (d['left'][i] + d['width'][i]) / dx
        y1 = (d['top'][i] + d['height'][i]) / dy

        boxB = [x0, y0, x1, y1]
        
        iou = bb_intersection_over_union(boxA, boxB)
        if iou > 0: 
            avaiablelist.append(i)

        if iou > maxvalue:
            index = i
            maxvalue = iou
            
    comb = combinations(avaiablelist, min(len(avaiablelist) ,3) ) 
    (x,y,w,h)=(0,0,0,0)

    # Print the obtained combinations 
    for pi in list(comb): 
        print (pi)
        listx0 = []
        listy0 = []
        listx1 = []
        listy1 = []

        for i in pi:
            listx0.append(d['left'][i] / dx)
            listy0.append(d['top'][i] / dy)
            listx1.append((d['left'][i] + d['width'][i]) / dx)
            listy1.append((d['top'][i] + d['height'][i]) / dy)
        
        
        # ---
        x0 = min(listx0)
        y0 = min(listy0)
        x1 = max(listx1)
        y1 = max(listy1)

        boxB = [x0, y0, x1, y1]
        
        iou = bb_intersection_over_union(boxA, boxB)
        if iou > maxvalue:
            maxvalue = iou
            x = int(x0)
            y = int(y0)
            xn = int(x1)
            yn = int(y1)
        # --- only x
        x0 = min(listx0)
        y0 = boxA[1]
        x1 = max(listx1)
        y1 = boxA[3]

        boxB = [x0, y0, x1, y1]
        
        iou = bb_intersection_over_union(boxA, boxB)
        if iou > maxvalue:
            maxvalue = iou
            x = int(x0)
            y = int(y0)
            xn = int(x1)
            yn = int(y1)
        # --- onlyy
        x0 = boxA[0]
        y0 = min(listy0)
        x1 = boxA[2]
        y1 = max(listy1)

        boxB = [x0, y0, x1, y1]
        
        iou = bb_intersection_over_union(boxA, boxB)
        if iou > maxvalue:
            maxvalue = iou
            x = int(x0)
            y = int(y0)
            xn = int(x1)
            yn = int(y1)
    cv2.rectangle(img, (x, y), (xn, yn), (0, 255, 0), 2)


cv2.imshow('img', img)

## _case_ use image.jpb
## _case2_ use invoce-sample.jpg

## current write the json
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
cv2.waitKey(0)