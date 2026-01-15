# Конспект: Сложные типы в SQL

## 1. Доступ к данным
* **Struct (`.`):** `col.field`
* **Array (`[]`):** `col[0]` (индекс с 0)
* **Map (`[]`):** `col['key_name']`

## 2. Функции
* `size(col)`: Количество элементов в массиве/мапе.
* `array_contains(col, value)`: Проверка наличия (Boolean).
* `element_at(col, index/key)`: Безопасное получение элемента (индексация с 1!).

## 3. Explode (Разворачивание)
Превращает вложенность в строки.
```sql
SELECT id, item FROM table LATERAL VIEW explode(items) t AS item
-- Или упрощенно в Spark 3:
SELECT id, explode(items) as item FROM table
