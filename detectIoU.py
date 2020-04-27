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
for p in data['blocks']:
    boxA = [p['left'], p['top'], p['left'] + p['width'], p['top'] + p['height'] ]

    index = -1
    maxvalue = 0

    for i in range(n_boxes):
        x0 = d['left'][i] / dx
        y0 = d['top'][i] / dy
        x1 = (d['left'][i] + d['width'][i]) / dx
        y1 = (d['top'][i] + d['height'][i]) / dy

        boxB = [x0, y0, x1, y1]
        
        iou = bb_intersection_over_union(boxA, boxB)
        if iou > maxvalue:
            index = i
            maxvalue = iou
    if index > -1 :
        # print(d['level'][i])
        (x, y, w, h) = (d['left'][index], d['top'][index], d['width'][index], d['height'][index])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)



cv2.imshow('img', img)

## _case_ use image.jpb
## _case2_ use invoce-sample.jpg

## current write the json
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
cv2.waitKey(0)