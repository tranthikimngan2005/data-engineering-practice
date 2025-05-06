import os
import json
import csv
import glob

def lam_phang_json(obj, cha=''):
    ket_qua = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            ten_moi = f"{cha}_{k}" if cha else k
            ket_qua.update(lam_phang_json(v, ten_moi))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            ten_moi = f"{cha}_{i}"
            ket_qua.update(lam_phang_json(v, ten_moi))
    else:
        ket_qua[cha] = obj
    return ket_qua

def chuyen_doi_json_sang_csv(duong_dan_json):
    with open(duong_dan_json, 'r', encoding='utf-8') as f:
        du_lieu = json.load(f)

    if isinstance(du_lieu, dict):
        du_lieu = [du_lieu]  # Nếu chỉ có 1 object

    du_lieu_phang = [lam_phang_json(item) for item in du_lieu]

    ten_csv = duong_dan_json.replace('.json', '.csv')
    with open(ten_csv, 'w', newline='', encoding='utf-8') as csvfile:
        if du_lieu_phang:
            truong = du_lieu_phang[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=truong)
            writer.writeheader()
            writer.writerows(du_lieu_phang)

    print(f"✔ Đã chuyển: {duong_dan_json} → {ten_csv}")

def main():
    duong_dan = 'data'
    danh_sach_file_json = glob.glob(f'{duong_dan}/**/*.json', recursive=True)

    if not danh_sach_file_json:
        print("❗ Không tìm thấy file JSON nào.")
        return

    for file_json in danh_sach_file_json:
        try:
            chuyen_doi_json_sang_csv(file_json)
        except Exception as e:
            print(f"⚠️ Lỗi với file {file_json}: {e}")

if __name__ == "__main__":
    main()
