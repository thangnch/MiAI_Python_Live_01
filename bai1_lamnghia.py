import cv2
import os

# Em muốn tạo thư mục và lưu vào đó 100 ảnh tự động.
# VD chỉ cần chạy đoạn code cái nó hỏi là bạn muốn tạo thư mục gì, nhập tên thưc mục,
# sau khi nhập xong ảnh tự lưu vào thư mục, a được lấy từ webcam. Cảm ơn a thắng

folder = input("Nhap vao ten thu muc:")
print("Thu muc luu anh:", folder)

if not os.path.exists(folder):
    os.mkdir(folder)


N = 100  # So anh can luu
count = 0

# Doc tu camera co id = 0
camera = cv2.VideoCapture(0)

while count <= N:
    # Doc tu webcam
    ret, image = camera.read()

    if ret:
        cv2.imshow("Camera", image)

        # Tang bien dem, tao duong dan den file
        count = count + 1
        file_name = "anh" + str(count) + ".png"
        file_path = os.path.join(folder, file_name)

        # Luu anh vao folder
        cv2.imwrite(file_path, image)

        if cv2.waitKey(1) == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()
