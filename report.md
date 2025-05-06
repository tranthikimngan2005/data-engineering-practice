
## Bài tập 1 - Tải và Giải nén Tệp tin

**Mục tiêu:**  
Kiểm tra khả năng tải các tệp `.zip` từ một nguồn HTTP và giải nén bằng Python.

**Các bước thực hiện:**
1. Truy cập thư mục `Exercises/Exercise-1`.
2. Đọc file `README.md` trong thư mục để hiểu yêu cầu chi tiết.
3. Sử dụng thư viện `requests` để tải file ZIP từ một đường dẫn cụ thể.
4. Dùng `zipfile` hoặc `shutil` để giải nén nội dung.
5. Lưu nội dung giải nén vào một thư mục cục bộ.
6. In thông báo thành công hoặc ghi log.

---

## Bài tập 2 - Web Scraping + Tải dữ liệu + Phân tích bằng Pandas

**Mục tiêu:**  
Thực hiện Web Scraping, xây dựng đường dẫn tải dữ liệu, và sử dụng Pandas để phân tích đơn giản.

**Các bước thực hiện:**
1. Truy cập thư mục `Exercises/Exercise-2`.
2. Dùng thư viện `requests` và `BeautifulSoup` để thu thập dữ liệu từ trang web.
3. Trích xuất danh sách liên kết tệp cần tải.
4. Dùng `requests` để tải các file về.
5. Đọc dữ liệu bằng `pandas.read_csv()` hoặc `read_excel()`.
6. Thực hiện các phép tính như: tổng (`sum()`), trung bình (`mean()`), nhóm (`groupby()`).
7. Ghi kết quả phân tích vào file CSV đầu ra.

---

##  Bài tập 3 - Làm việc với AWS S3 bằng Boto3

**Mục tiêu:**  
Sử dụng thư viện `boto3` để truy cập và tải dữ liệu từ các bucket công khai trên AWS S3.

**Các bước thực hiện:**
1. Truy cập thư mục `Exercises/Exercise-3`.
2. Cài đặt thư viện `boto3` và cấu hình AWS nếu cần.
3. Xác định bucket và danh sách tệp trong README.
4. Dùng `boto3.client('s3')` để liệt kê và tải các tệp cần thiết.
5. Lưu các tệp vào thư mục cục bộ.
6. Kiểm tra nội dung (ví dụ: in ra kích thước tệp hoặc 5 dòng đầu tiên).

---

## Bài tập 4 - Duyệt thư mục & Chuyển đổi JSON sang CSV

**Mục tiêu:**  
Duyệt cấu trúc thư mục lồng nhau, tìm các file `.json`, và chuyển đổi nội dung thành `.csv`.

**Các bước thực hiện:**
1. Truy cập thư mục `Exercises/Exercise-4`.
2. Dùng `os.walk()` để duyệt toàn bộ thư mục và tìm các file `.json`.
3. Với mỗi file JSON:
   - Đọc nội dung bằng `json.load()`.
   - Chuyển đổi sang dạng bảng phù hợp với CSV.
   - Ghi file `.csv` tương ứng vào thư mục khác.
4. Ghi log các file đã xử lý và bỏ qua các file lỗi định dạng.

---

## Bài tập 5 - Thiết kế Mô hình Dữ liệu cho PostgreSQL bằng Python

**Mục tiêu:**  
Dựa vào các file CSV, thiết kế lược đồ dữ liệu, tạo bảng, và nạp dữ liệu vào PostgreSQL bằng Python.

**Các bước thực hiện:**
1. Truy cập thư mục `Exercises/Exercise-5`.
2. Khám phá nội dung các file `.csv` để xác định quan hệ giữa các bảng.
3. Viết câu lệnh SQL để tạo bảng (`CREATE TABLE`) và thêm các chỉ mục (`INDEX`).
4. Dùng `psycopg2` hoặc `SQLAlchemy` để kết nối với PostgreSQL.
5. Tạo bảng trong cơ sở dữ liệu.
6. Đọc dữ liệu từ CSV và insert vào các bảng.
7. Thực hiện một số truy vấn kiểm tra như: đếm số dòng, kiểm tra ràng buộc khóa chính.
8. Lưu lại thiết kế schema trong file `schema.sql` hoặc tài liệu markdown.


## Bài tập 6 - Nhập Dữ Liệu và Tổng Hợp với PySpark

**Mục tiêu:**  
Sử dụng PySpark để xử lý và tổng hợp dữ liệu lớn từ các tệp CSV.

**Các bước thực hiện:**

1. Truy cập thư mục `Exercises/Exercise-6`.

2. Xây dựng Docker image bằng lệnh:
   ```bash
   docker build --tag=exercise-6 .
````

3. Thực hiện kiểm tra thử với lệnh sau để chạy Docker container:

   ```bash
   docker-compose up run
   ```

4. Thực hiện nhập dữ liệu từ các tệp `.zip` trong thư mục `data`. Các tệp này cần được giữ nguyên trạng thái nén trong suốt quá trình xử lý.

5. Dùng PySpark để giải nén và đọc dữ liệu từ các tệp CSV, sử dụng `spark.read.csv()` hoặc các phương thức thích hợp khác.

6. Tiến hành các bước xử lý dữ liệu cần thiết: lọc, nhóm, tính toán tổng hợp, v.v.

7. In kết quả hoặc lưu dữ liệu đã xử lý vào một tệp đầu ra, chẳng hạn như CSV hoặc Parquet.

## Bài tập 7 - Sử dụng Các Hàm PySpark Khác Nhau

**Mục tiêu:**  

Giải quyết bài toán sử dụng các hàm có sẵn trong `spark.sql.functions`, không sử dụng UDF hay các phương thức Python khác.

**Các bước thực hiện:**

1. Truy cập thư mục `Exercises/Exercise-7`.

2. Xây dựng Docker image bằng lệnh:

   ```bash
   docker build --tag=exercise-7 .
   ```

3. Thực hiện kiểm tra thử với lệnh sau để chạy Docker container:

   ```bash
   docker-compose up run
   ```

4. Thực hiện nhập dữ liệu từ tệp `hard-drive-2022-01-01-failures.csv.zip` trong thư mục `data`. Tệp này cần được giữ nguyên trạng thái nén trong suốt quá trình xử lý.

5. Dùng PySpark để giải nén và đọc dữ liệu từ tệp `.csv` nén.

6. Sử dụng các hàm trong `spark.sql.functions` để xử lý dữ liệu, bao gồm:

   * **Lọc dữ liệu:** sử dụng `filter()` hoặc `where()`.
   * **Tính toán tổng hợp:** sử dụng `sum()`, `avg()`, `count()`, v.v.
   * **Nhóm dữ liệu:** sử dụng `groupBy()` và các hàm nhóm khác.
   * **Chuyển đổi dữ liệu:** sử dụng các hàm như `withColumn()`, `cast()`, v.v.

7. In kết quả hoặc lưu dữ liệu đã xử lý vào tệp đầu ra.



## Thành viên thực hiện

- **Trần Thị Kim Ngân – 23791511**  
- **Trần Quốc Sang – 23715111**

## ✅ Link GitHub

[https://github.com/tranthikimngan2005/data-engineering-practice](https://github.com/tranthikimngan2005/data-engineering-practice)

---

