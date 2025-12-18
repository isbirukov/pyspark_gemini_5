# Конспект: Трансформации (Narrow vs Wide)

## 1. Типы зависимостей
* **Narrow (Узкие):** Результат зависит от одного раздела родителя. Нет обмена данными.
    * `select`, `filter`, `withColumn`, `map`.
* **Wide (Широкие):** Результат зависит от многих разделов. Вызывает **Shuffle**.
    * `groupBy`, `orderBy`, `join`, `distinct`.

## 2. Модуль Functions
`from pyspark.sql import functions as F`
* `F.col("col_name")` — ссылка на колонку.
* `F.lit(10)` — литерал (константа).
* `F.sum()`, `F.avg()`, `F.max()` — агрегации.

## 3. Best Practices
1.  **Filter Early:** Фильтруй данные как можно раньше, чтобы уменьшить объем для Shuffle.
2.  **Избегай лишних сортировок:** `orderBy` — одна из самых дорогих операций.
3.  **Используй `explain()`:** Если видишь "Exchange" там, где не ожидал — ищи скрытый Shuffle.
