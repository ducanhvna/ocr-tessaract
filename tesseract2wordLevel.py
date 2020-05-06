# conver tesseract 2 word level
# Step by step
#   Step 1: Use tesseract recognition
#   Step 2: convert all text block to list
# List all file

import pytesseract
from pytesseract import Output
import cv2
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
import glob

def ExtractData(folderpath, outputfolder):

    # Step 1: Use tesseract reconition
    # Step 2: convert all text block to list

    foldername = os.path.basename(folderpath)
    mylist =  [item for sublist in [glob.glob(folderpath + ext) for ext in ["/*.png", "/*.jpg"]] for item in sublist]


    for filepath in mylist:
        foldername = os.path.basename(os.path.splitext(filepath)[0])
        # Load Image
        img = cv2.imread('image.jpg')
        # get dimensions of image
        dimensions = img.shape
        
        # height, width, number of channels in image
        imgheight = img.shape[0]
        imgwidth = img.shape[1]
        imgchannels = img.shape[2]
        # print('Image Dimension    : ',imgdimensions)
        print('Image Height       : ',imgheight)
        print('Image Width        : ',imgwidth)
       
        d = pytesseract.image_to_data(img, output_type=Output.DICT)

        ## Incase print all
        # d = pytesseract.image_to_data(img, output_type=Output.DICT)

        data = ET.Element('annotation')
        folder = ET.SubElement(data, 'folder')
        folder.text = 'windows_v1.8.0'
        
        filename = ET.SubElement(data, 'filename')
        path = ET.SubElement(data, 'path')
        source = ET.SubElement(data, 'source')

        database = ET.SubElement(source, 'database')
        database.text = 'Unknown'

        # document common info
        # size
        size = ET.SubElement(data, 'size')
        width = ET.SubElement(size, 'width')
        
        width.text = str(imgwidth)
        

        height = ET.SubElement(size, 'height')
        height.text = str(imgheight)
        
        # fixed deep to 3
        depth = ET.SubElement(size, 'depth')
        depth.text = '3'

        # fixed segmented to 0
        segmented = ET.SubElement(data, 'segmented')
        segmented.text = '0'

        # number of textblock
        n_boxes = len(d['level'])

        print ('level: ',n_boxes)
        for i in range(n_boxes):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # add contrain for conf

        n_boxes = len(d['text'])
        n_boxes = len(d['level'])
        print ('level: ',n_boxes)
        
        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        keys = list(d.keys())

        n_boxes = len(d['text'])

        print (' ************** level: ',n_boxes)

        filelines = []
        for i in range(n_boxes):
            print(d['text'][i] + '\n')
            if  (d['text'][i].strip() != '') and (int(d['conf'][i]) > 10):
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


                # each char add 1 element
                chardisplay = d['text'][i]
                objectele = ET.SubElement(data, 'object')
                name = ET.SubElement(objectele, 'name')
                name.text = chardisplay

                pose = ET.SubElement(objectele, 'pose')
                pose.text = 'Unspecified'

                truncated = ET.SubElement(objectele, 'truncated')
                truncated.text = '0'

                difficult = ET.SubElement(objectele, 'difficult')
                difficult.text = '0'

                bndbox = ET.SubElement(objectele, 'bndbox')
                xmin = ET.SubElement(bndbox, 'xmin')
                xmin.text = str(x)

                ymin = ET.SubElement(bndbox, 'ymin')
                ymin.text = str(y)

                xmax = ET.SubElement(bndbox, 'xmax')
                xmax.text = str(x + w)

                ymax = ET.SubElement(bndbox, 'ymax')
                ymax.text = str(y+ h)

                content = xmin.text + ',' + ymin.text + ',' + xmax.text + "," + ymin.text + "," + xmax.text + "," + ymax.text + "," + xmin.text + "," + ymax.text + "," + name.text
                filelines.append(content)

        mydata = ET.tostring(data)
        myfile = open(outputfolder + "/" + foldername + ".xml", "wb")

        myfile.write(mydata)

        with open(outputfolder + "/" + foldername + '.txt', 'w') as f:
            for item in filelines:
                f.write("%s\n" % item)

inputfolder = 'Images'
outputfoder = 'testTesseract2Word'
# Create Output foder if not exsts

if not os.path.exists(outputfoder):
    os.makedirs(outputfoder)
ExtractData(inputfolder, outputfoder)