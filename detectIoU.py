##########
# Overview
#   Bài toán đặt ra là từ một tập format có sẵn gọi là meta format chúng ta cần biết là
#   Text dó thược block nào. như vậy trước tiên chúng ta cần xác định vị trí của một text block
# Meta Format
#   Meta format là thông tin lưu trữ cấu trúc của một văn bản, bao gồm thông về kích thước chiều dài,
#   Chiều rông, thông tin về format id, thông tin cấu trúc của văn bản đó trước tiên ta xác định 
#   được 1 block array từ một văn bản. Như vậy chúng ta có định như sau
[
  {
      formatid: 1,
      width : 1024,
      heigh: 800
      Blockes: [
          {
              x: 50,
              y: 50, 
              width = 50,
               heigh = 100
            }

        ]


  }
]

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


# Load Image
# use tessaract detect image

# B3 duyệt tất cả cac block trong meta format
#           Tìm block nào có IoU cao nhất trong các block ảnh
#            Vẽ block đó