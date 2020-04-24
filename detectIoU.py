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