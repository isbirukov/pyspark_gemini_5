# Конспект: UDF и Pandas UDF

## 1. Иерархия производительности
1.  **Native Spark (`F` functions):** Самые быстрые. Выполняются в JVM.
2.  **Pandas UDF (Vectorized):** Быстрые. Используют Apache Arrow. Передают данные блоками.
3.  **Standard Python UDF:** Медленные. Сериализация (Pickle). Построчное выполнение.

## 2. Pandas UDF
Требует `pyarrow`.
```python
@pandas_udf("double")
def add_one(s: pd.Series) -> pd.Series:
    return s + 1
