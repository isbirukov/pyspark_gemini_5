# Конспект: Основы DataFrame

## 1. Определение
DataFrame — это распределенная коллекция данных, организованная в именованные колонки. Аналог таблицы в РСУБД.

## 2. Схема (Schema)
Описание структуры данных.
* **StructType:** Коллекция полей (вся таблица).
* **StructField:** Одно поле (Имя, Тип, Nullable).

Пример:
```python
schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), True)
])
