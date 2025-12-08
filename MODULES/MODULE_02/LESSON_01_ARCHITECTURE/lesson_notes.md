# Конспект Модуля 2: Архитектура Spark

## Иерархия
$$Application \rightarrow Job \rightarrow Stage \rightarrow Task$$

* **Job** создается при вызове **Action** (count, save, show).
* **Stage** создается, когда требуется **Shuffle** (передача данных между узлами).
* **Task** — единица работы над одним партицием данных.

## Компоненты
* **Driver:** Мозг. Строит DAG.
* **Executor:** Мышцы. Выполняет Tasks.

## Best Practice
* Использовать Spark UI (порт 4040) для анализа.
* Избегать `collect()` на больших данных.
* Понимать, какие операции вызывают Shuffle (groupBy, join, repartition).
