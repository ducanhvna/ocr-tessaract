# ocr-tessaract
 
# Overview
### Intersection over Union for object detection

In the remainder of this blog post I’ll explain what the Intersection over Union evaluation metric is and why we use it.

I’ll also provide a Python implementation of Intersection over Union that you can use when evaluating your own custom object detectors.

Finally, we’ll look at some actual results of applying the Intersection over Union evaluation metric to a set of ground-truth and predicted bounding boxes.

# Idea
Build meta data by lableImage tool

[! build meta data data by lbl Image tool](Images/BuildMetadata.png)

Convert to json fomat

```bash
[
    {
        "formatid":1,
        "width" : 1024,
        "heigh": 800,
        "Blockes": [
            {
                "x": 50,
                "y": 50, 
                "width" : 50,
                "heigh" : 100
              }
  
          ]
    }
] 

```

# Installation
```bash
pip install -r requirements.txt
python detecIoU.py
```

# Result
## Solution 1: Use only one area (textblock) - which has maximum IoU value 

[!Solution 1](Images/savedImageSolution1.jpg)

## Solution 2: Use cobination 3 of block to bulid result

[!Solution 2](Images/savedImageSolution5.jpg)

# references
[!Intersection over Union (IoU) for object detection](https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)

[!Reading and Writing JSON to a File in Python](https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/)