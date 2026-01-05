# Конспект: Оконные Функции

## 1. Концепция
Позволяют считать агрегаты и ранги в контексте "соседей" строки, не меняя количество строк в DataFrame.

## 2. Синтаксис
```python
w = Window.partitionBy("group_col").orderBy("sort_col")
df.withColumn("rank", F.rank().over(w))
```

## 3. Основные функции
Rank:
- row_number(): Уникальный номер (1, 2, 3).
- rank(): С пропусками (1, 1, 3).
- dense_rank(): Без пропусков (1, 1, 2).

Offset:
- lag(col, n): Значение n строк назад.
- lead(col, n): Значение n строк вперед.

Aggregates:
- sum().over(w), avg().over(w).

## 4. Границы окна (Frames)
rowsBetween(start, end)
- Window.unboundedPreceding: Начало раздела.
- Window.currentRow: Текущая строка.
- Window.unboundedFollowing: Конец раздела.
- Пример Running Total: rowsBetween(Window.unboundedPreceding, Window.currentRow).
