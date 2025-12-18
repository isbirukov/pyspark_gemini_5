# Конспект: Типы данных и Null

## 1. Casting (Приведение типов)
`df.select(F.col("age").cast("integer"))`
* Если приведение невозможно (строка "abc" в int), Spark вернет `null` (безопасно).

## 2. Null Safety
* **Арифметика:** `5 + Null = Null`. Всегда защищайте числовые поля.
* **Проверка:** `.filter(F.col("x").isNull())`.
* **Замена:**
    * `F.coalesce(col1, col2)`: Возвращает первый не-Null.
    * `df.na.fill(0)`: Заменяет все Null на константу.
    * `df.na.drop()`: Удаляет строки с Null.

## 3. Даты
* `F.to_date(col, format)`: Строка -> Дата.
* Форматы: `yyyy-MM-dd`, `dd/MM/yyyy`. Буквы регистра зависимы (MM - месяц, mm - минуты).
