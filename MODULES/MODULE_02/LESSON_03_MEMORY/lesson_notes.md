# Конспект: Управление Памятью (Memory Management)

## Структура Unified Memory
1. **Reserved (300MB):** Системная.
2. **User Memory (40%):** Метаданные, UDF.
3. **Spark Memory (60%):**
   * **Storage (50%):** Кэш (`.cache()`), Broadcast.
   * **Execution (50%):** Shuffles, Joins, Sorts.

*Граница между Storage и Execution подвижная.*

## Проблемы
* **Spill to Disk:** Когда не хватает Execution Memory, данные пишутся на диск. Очень медленно.
* **GC Overhead:** Когда создается слишком много объектов, уборщик мусора останавливает работу (Stop-the-world).
* **OOM:** Память кончилась полностью.

## Best Practices
* Не кэшировать данные, которые используются 1 раз.
* Следить за GC Time в UI.
* Увеличивать `spark.executor.memory`, если есть Spill.
