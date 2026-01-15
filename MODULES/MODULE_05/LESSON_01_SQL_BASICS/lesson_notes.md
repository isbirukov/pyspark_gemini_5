# Конспект: Основы Spark SQL

## 1. Интеграция
Spark SQL и DataFrame API — это два интерфейса к одному движку.
`spark.sql(...)` возвращает DataFrame, который можно дальше трансформировать методами API (`.filter`, `.join`).

## 2. Views (Представления)
Чтобы DataFrame стал доступен в SQL, его нужно зарегистрировать:
```python
df.createOrReplaceTempView("my_table")
