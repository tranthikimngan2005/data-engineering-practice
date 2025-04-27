import requests
from bs4 import BeautifulSoup
import pandas as pd
URL = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
TARGET_DATETIME = "2024-01-19 10:27"

def get_file_link():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    for row in soup.find_all('tr'):
        if TARGET_DATETIME in row.text:
            return row.find('a')['href']
    return None

def download_file(file_link):
    file_url = URL + file_link
    response = requests.get(file_url)
    local_filename = "weather_data.csv"
    with open(local_filename, 'wb') as f:
        f.write(response.content)
    return local_filename

def analyze_file(filename):
    try:
        df = pd.read_csv(filename)
        if 'HourlyDryBulbTemperature' not in df.columns:
            print("Không tìm thấy cột HourlyDryBulbTemperature.")
            print(f"Các cột hiện có: {df.columns.tolist()}")
            return

        max_temp = df['HourlyDryBulbTemperature'].max()
        hottest_records = df[df['HourlyDryBulbTemperature'] == max_temp]
        print("🔺 Các bản ghi có nhiệt độ cao nhất:")
        print(hottest_records)
    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc file: {e}")

def main():
    print("🔍 Đang tìm file theo ngày chỉnh sửa...")
    file_link = get_file_link()
    if file_link:
        print(f"📄 Đã tìm thấy file: {file_link}")
        filename = download_file(file_link)
        print(f"⬇️ Đã tải về file: {filename}")
        analyze_file(filename)
    else:
        print("❌ Không tìm thấy file với thời gian được chỉ định.")

if __name__ == "__main__":
    main()
