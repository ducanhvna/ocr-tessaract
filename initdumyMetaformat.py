# Nhiệm vụ của file là khởi tạo một bộ meta format từ nội dung của tessarac
# lấy các thông tin của tessaract và in ra text block theo các level
# Đầu vào của phương pháp là một ảnh
# Đầu ra của phương pháp là một bộ meta format theo các level cua ảnh

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
cv2.waitKey(0)
#cv2.imwrite('_8_level_case_value1.jpg',img)

