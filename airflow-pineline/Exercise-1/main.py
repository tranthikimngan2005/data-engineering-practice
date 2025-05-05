import os
import requests
import zipfile

# Danh sách các đường dẫn URL chứa các tệp dữ liệu zip
danh_sach_duong_dan = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

# Hàm để tải xuống và giải nén một tệp zip từ URL
def tai_tap_tin(duong_dan, thu_muc_tai_xuong):
    ten_tap_tin = duong_dan.split('/')[-1]
    duong_dan_zip = os.path.join(thu_muc_tai_xuong, ten_tap_tin)

    # Gửi yêu cầu tải xuống
    print(f"Đang tải xuống tệp: {ten_tap_tin}")
    phan_hoi = requests.get(duong_dan)

    if phan_hoi.status_code == 200:
        with open(duong_dan_zip, 'wb') as tep:
            tep.write(phan_hoi.content)
        print(f"Tải xuống {ten_tap_tin} thành công!")
    else:
        print(f"Tải xuống {ten_tap_tin} thất bại với mã lỗi {phan_hoi.status_code}")
        return

    # Giải nén tệp zip sau khi tải
    giai_nen_csv(duong_dan_zip, thu_muc_tai_xuong)

# Hàm để giải nén tệp zip và xóa nó sau khi hoàn tất
def giai_nen_csv(duong_dan_zip, thu_muc_tai_xuong):
    with zipfile.ZipFile(duong_dan_zip, 'r') as tep_zip:
        # Giải nén tất cả các tệp vào thư mục đích
        tep_zip.extractall(thu_muc_tai_xuong)
        print(f"Đã giải nén tệp {duong_dan_zip}")

    # Xóa tệp zip sau khi giải nén xong
    os.remove(duong_dan_zip)
    print(f"Đã xóa tệp zip {duong_dan_zip}")

# Hàm chính để điều phối toàn bộ quá trình
def main():
    thu_muc_tai_xuong = 'downloads'
    if not os.path.exists(thu_muc_tai_xuong):
        os.makedirs(thu_muc_tai_xuong)
        print(f"Đã tạo thư mục {thu_muc_tai_xuong}")

    # Tải và giải nén từng tệp trong danh sách
    for duong_dan in danh_sach_duong_dan:
        tai_tap_tin(duong_dan, thu_muc_tai_xuong)

# Chạy hàm chính nếu file được chạy trực tiếp
if __name__ == '__main__':
    main()
