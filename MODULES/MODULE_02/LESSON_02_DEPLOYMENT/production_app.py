import sys
from pyspark.sql import SparkSession
import time

def main():
    # 1. Инициализация (без hardcode настроек, они придут из spark-submit)
    spark = SparkSession.builder.getOrCreate()
    
    # Получаем аргументы командной строки
    # sys.argv[0] - это имя скрипта
    if len(sys.argv) > 1:
        app_name_suffix = sys.argv[1]
    else:
        app_name_suffix = "Default"

    print(f"🚀 Запуск приложения: Production_App_{app_name_suffix}")
    
    # 2. Логика (пример)
    # Генерируем данные
    data = spark.range(0, 1000000)
    
    # Трансформация
    res = data.selectExpr("id * 5 as id_mult").filter("id_mult > 100")
    
    # Action
    count = res.count()
    
    print(f"📊 Результат подсчета: {count}")
    
    # Имитация долгой работы, чтобы успеть посмотреть в UI
    print("⏳ Спим 30 секунд (проверьте Spark UI)...")
    time.sleep(30)
    
    spark.stop()
    print("✅ Работа завершена.")

if __name__ == "__main__":
    main()