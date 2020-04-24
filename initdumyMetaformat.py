# Nhiệm vụ của file là khởi tạo một bộ meta format từ nội dung của tessarac
# lấy các thông tin của tessaract và in ra text block theo các level
# Đầu vào của phương pháp là một ảnh
# Đầu ra của phương pháp là một bộ meta format theo các level cua ảnh

######
# Hàm ghi file ra json. Đầu vào của ham là các thông tin width, heigh và thông tin cac  block
######
import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

### hàm read file 
# with open('data.txt') as json_file:
#     data = json.load(json_file)
#     for p in data['people']:
#         print('Name: ' + p['name'])
#         print('Website: ' + p['website'])
#         print('From: ' + p['from'])
#         print('')

# bước 1 thử ảnh đầu vào là image.jpg


import re
import pytesseract
from pytesseract import Output
import cv2
img = cv2.imread('image.jpg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)

custom_config = r'--oem 1 --psm 6'
print(pytesseract.image_to_string(img, config=custom_config))

n_boxes = len(d['level'])
# print ('level: ',n_boxes)
# for i in range(n_boxes):
#     if d['text'][i].strip() != '' :
#         # print(d['level'][i])
#     	(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#     	cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

## Level case

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d['level'])

## Now Initialize json data

# n_boxes = len(d['level'])
print ('level: ',n_boxes)
for i in range(n_boxes):
    if d['level'][i] == 5 :
        print(d['text'][i])
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)

## _case_ use image.jpb
## _case2_ use invoce-sample.jpg

## current write the json
width = img.size().width 
height = img.size().height





cv2.waitKey(0)
#cv2.imwrite('_8_level_case_value1.jpg',img)



