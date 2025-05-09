
#LAB8 - 
##  Mục tiêu dự án

Xây dựng một pipeline xử lý dữ liệu theo mô hình **ELT** sử dụng các công cụ:

- **Apache Airflow**: quản lý luồng công việc (workflow)
- **MySQL**: lưu trữ dữ liệu thô
- **PostgreSQL**: lưu trữ dữ liệu đã xử lý
- **Power BI**: trực quan hóa dữ liệu
- **Docker**: container hóa toàn bộ hệ thống để dễ dàng triển khai

---

## Cấu trúc dự án

```

data-engineering-practice/
└── LAB8/
├── dags/
│   └── etl\_pipeline.py           # DAG Airflow
├── dataset/                      # Dữ liệu CSV đầu vào
│   ├── customers.csv
│   ├── orders.csv
│   └── ...
├── load\_dataset\_into\_mysql/     # Python script tải dữ liệu vào MySQL
├── query.sql                    # Truy vấn SQL xử lý dữ liệu trong PostgreSQL
├── Sales\_Overview\.pbix          # File báo cáo Power BI
├── Dockerfile
└── docker-compose.yaml

````

---

## 🔄 Quy trình xử lý dữ liệu

```mermaid
flowchart LR
    A[CSV File] --> B[Python Script]
    B --> C[MySQL]
    C --> D[Airflow - Load Task]
    D --> E[PostgreSQL]
    E --> F[Power BI Report]
````

1. **Extract**: Đọc dữ liệu từ CSV bằng Python
2. **Load**: Ghi dữ liệu vào MySQL
3. **Transform**: Di chuyển dữ liệu từ MySQL sang PostgreSQL và thực hiện xử lý
4. **Visualize**: Kết nối Power BI với PostgreSQL để tạo báo cáo

---

## ⚙️ Các thành phần chi tiết

### 1. Dữ liệu đầu vào (`dataset/`)

* Gồm các file CSV như:

  * `customers.csv`
  * `orders.csv`
  * `products.csv`
  * `order_details.csv`

### 2. Tải dữ liệu vào MySQL (`load_dataset_into_mysql/`)

* Sử dụng `pandas` và `sqlalchemy` để:

  * Đọc file CSV
  * Ghi dữ liệu vào bảng MySQL
* Ví dụ:

```python
df = pd.read_csv("customers.csv")
df.to_sql("customers", con=engine, if_exists="replace", index=False)
```

### 3. Airflow DAG (`dags/etl_pipeline.py`)

* Các bước DAG:

  * `start_pipeline` → `extract` → `load` → `transform` → `end_pipeline`

### 4. Xử lý dữ liệu (`query.sql`)

* Tạo bảng, chèn dữ liệu, xử lý:

```sql
SELECT customer_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id;
```

### 5. Trực quan hóa (`Sales_Overview.pbix`)

* Báo cáo Power BI gồm:

  * Doanh thu theo tháng
  * Sản phẩm bán chạy nhất
  * Khách hàng tiềm năng

### 6. Docker & docker-compose

* Cấu hình khởi tạo:

```bash
docker-compose up --build
```

---

## 📊 Kết quả

* Dữ liệu thô → MySQL
* Dữ liệu đã xử lý → PostgreSQL
* Báo cáo → Power BI
