import os
import requests
import zipfile

# Danh sách URL
download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",  # URL sai
]

# Tạo thư mục downloads nếu chưa tồn tại
downloads_dir = "downloads"
os.makedirs(downloads_dir, exist_ok=True)

# Tải và giải nén
for url in download_uris:
    filename = url.split("/")[-1]
    zip_path = os.path.join(downloads_dir, filename)

    try:
        print(f"Tải {filename} ...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Ghi nội dung file zip
        with open(zip_path, "wb") as f:
            f.write(response.content)

        # Giải nén
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(downloads_dir)

        # Xóa file zip sau khi giải nén
        os.remove(zip_path)
        print(f"✓ Hoàn tất: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Lỗi tải {url}: {e}")
    except zipfile.BadZipFile as e:
        print(f"✗ Lỗi giải nén {filename}: {e}")
