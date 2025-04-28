import os
import requests
import zipfile

urls = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def download_file(url, download_folder):
    # Lấy tên tệp từ URL (lấy phần sau dấu / cuối cùng)
    filename = url.split('/')[-1]

    # Đường dẫn lưu tệp zip
    zip_file_path = os.path.join(download_folder, filename)

    # Tải tệp zip
    print(f"Đang tải xuống tệp: {filename}")
    response = requests.get(url)

    if response.status_code == 200:
        with open(zip_file_path, 'wb') as f:
            f.write(response.content)
        print(f"Tải xuống {filename} thành công!")
    else:
        print(f"Tải xuống {filename} thất bại với mã lỗi {response.status_code}")
        return

    # Giải nén tệp zip
    extract_csv(zip_file_path, download_folder)

# Hàm để giải nén tệp zip và lấy tệp CSV
def extract_csv(zip_file_path, download_folder):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Giải nén tất cả tệp vào thư mục downloads
        zip_ref.extractall(download_folder)
        print(f"Đã giải nén tệp {zip_file_path}")

    # Xóa tệp zip sau khi giải nén
    os.remove(zip_file_path)
    print(f"Đã xóa tệp zip {zip_file_path}")

# Hàm chính để thực hiện các bước
def main():
    # Tạo thư mục downloads nếu chưa tồn tại
    download_folder = 'downloads'
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        print(f"Đã tạo thư mục {download_folder}")

    # Tải xuống và giải nén các tệp
    for url in urls:
        download_file(url, download_folder)

if __name__ == '__main__':
    main()