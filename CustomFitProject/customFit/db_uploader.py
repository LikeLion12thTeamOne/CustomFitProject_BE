import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()

from customFit.models import FoodCategory, Product

CSV_PATH = os.path.join(os.path.dirname(__file__), 'ProductDB.csv')

def load_csv_to_db():
    with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category_name = row['category']
            category, created = FoodCategory.objects.get_or_create(category_name=category_name)

            # 유효성 검사를 통해 기본값을 설정
            capacity = row['Capacity']
            if capacity == '-' or not capacity:
                capacity = 0.0  # 기본값 설정

            calories = row['calories']
            if calories == '-' or not calories:
                calories = 0.0  # 기본값 설정

            sodium = row['sodium']
            if sodium == '-' or not sodium:
                sodium = 0.0  # 기본값 설정

            sugars = row['sugars']
            if sugars == '-' or not sugars:
                sugars = 0.0  # 기본값 설정

            protein = row['protein']
            if protein == '-' or not protein:
                protein = 0.0  # 기본값 설정

            product = Product(
                product_name=row['product_name'],
                manufacturer=row['manufacturer'],
                Capacity=float(capacity),  # 문자열을 float으로 변환
                calories=float(calories),  # 문자열을 float으로 변환
                sodium=float(sodium),      # 문자열을 float으로 변환
                sugars=float(sugars),      # 문자열을 float으로 변환
                protein=float(protein),    # 문자열을 float으로 변환
                category=category
            )
            product.save()

if __name__ == "__main__":
    load_csv_to_db()
    print("CSV 데이터를 데이터베이스에 성공적으로 삽입했습니다.")
