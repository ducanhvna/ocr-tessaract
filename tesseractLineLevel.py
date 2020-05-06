from tesserocr import PyTessBaseAPI, RIL
import cv2

with PyTessBaseAPI() as api:
    api.SetImageFile('image.jpg')
    print(api.GetUTF8Text())

imagePath = 'image.jpg'

img = cv2.imread(imagePath)
with PyTessBaseAPI(psm=6, oem=1) as api:
    level = RIL.TEXTLINE
    api.SetImageFile(imagePath)
    api.Recognize()
    ri = api.GetIterator()
    while(ri.Next(level)):
        word = ri.GetUTF8Text(level)
        boxes = ri.BoundingBox(level)
        cv2.rectangle(img, (boxes[0], boxes[1]), (boxes[2], boxes[3]), (0, 255, 0), 2)
        print(word,"word")
        print(boxes,"coords")

cv2.imshow('img', img)
cv2.waitKey(0)