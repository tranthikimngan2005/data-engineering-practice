import requests
import gzip
import io

def tai_file_tu_s3_http(khoa: str) -> bytes:
    url = f"https://data.commoncrawl.org/{khoa}"  # Đảm bảo URL đúng
    print(f"Đang tải từ: {url}")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.content

def luu_du_lieu_vao_file(data: str, ten_file: str):
    with open(ten_file, 'a', encoding='utf-8') as file:  # Mở file ở chế độ thêm (append)
        file.write(data + "\n")

def chinh_chay():
    print("Bắt đầu quá trình...")
    khoa_gz = 'crawl-data/CC-MAIN-2023-50/wet.paths.gz'
    du_lieu_gz = tai_file_tu_s3_http(khoa_gz)
    print("Tệp đã tải thành công!")

    with gzip.GzipFile(fileobj=io.BytesIO(du_lieu_gz)) as gz_file:
        dong_dau_tien = gz_file.readline().decode('utf-8').strip()
        print(f"Khóa tệp WET đầu tiên: {dong_dau_tien}")

    du_lieu_wet = tai_file_tu_s3_http(dong_dau_tien)
    print("Tệp thứ hai đã tải thành công!")

    with gzip.GzipFile(fileobj=io.BytesIO(du_lieu_wet)) as wet_file:
        # Lưu 50 dòng đầu tiên vào file
        for i, dong in enumerate(wet_file):
            dong_giai_ma = dong.decode('utf-8').rstrip()
            print(dong_giai_ma)  # In ra màn hình
            luu_du_lieu_vao_file(dong_giai_ma, 'output.txt')  # Lưu vào tệp 'output.txt'
            if i > 50:  # Giới hạn in ra và lưu 50 dòng đầu tiên
                break

    print("Quá trình hoàn tất!")

if __name__ == '__main__':
    chinh_chay()
