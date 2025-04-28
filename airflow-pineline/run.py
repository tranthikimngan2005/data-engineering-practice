import os
import subprocess

BASE_DIR = os.getcwd()

for i in range(1, 6):
    exercise_dir = os.path.join(BASE_DIR, f"Exercise-{i}")
    print("=" * 40)
    print(f" Đang xử lý: {exercise_dir}")
    print("=" * 40)

    if not os.path.isdir(exercise_dir):
        print(f" Không tìm thấy thư mục {exercise_dir}")
        continue

    try:
        # Bước 1: docker build
        print(f" Building Docker image: exercise-{i}")
        subprocess.run(["docker", "build", "--tag", f"exercise-{i}", "."], cwd=exercise_dir, check=True)

        # Bước 2: docker-compose up run
        print(f" Running docker-compose for exercise-{i}")
        result = subprocess.run(
            ["docker", "compose", "up", "--build", "--no-start"],
            cwd=exercise_dir, check=True, capture_output=True, text=True
        )
        print(result.stdout)
        print(result.stderr)
        print(f" Hoàn thành Exercise-{i}\n")

    except subprocess.CalledProcessError as e:
        print(f"️ Lỗi khi xử lý Exercise-{i}: {e}\n")
