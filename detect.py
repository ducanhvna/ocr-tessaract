import re
import pytesseract
from pytesseract import Output
import cv2
img = cv2.imread('invoice-sample.jpg')

## Incase print all
# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# n_boxes = len(d['level'])
# print ('level: ',n_boxes)
# for i in range(n_boxes):
#     (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

## add contrain for conf

# n_boxes = len(d['text'])
# n_boxes = len(d['level'])
# print ('level: ',n_boxes)
# for i in range(n_boxes):
#     if int(d['conf'][i]) > 60:
#         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#         img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# keys = list(d.keys())

# date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'

# n_boxes = len(d['text'])

# print (' ************** level: ',n_boxes)
# for i in range(n_boxes):
#     print(d['text'][i] + '\n')
#     if int(d['conf'][i]) > 60:
#     	if re.match(date_pattern, d['text'][i]):
# 	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
# 	        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow('img', img)

d = pytesseract.image_to_data(img, output_type=Output.DICT)

custom_config = r'--oem 1 --psm 6'
print(pytesseract.image_to_string(img, config=custom_config))

# print(d['level'])
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
    if d['level'][i] == 1 :
        print(d['text'][i])
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)

## _case_ use image.jpb
## _case2_ use invoce-sample.jpg
cv2.waitKey(0)
#cv2.imwrite('_8_level_case_value1.jpg',img)


