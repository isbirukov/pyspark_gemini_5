# Конспект: Catalog и Tables

## 1. Managed Table (Управляемая)
* Spark управляет всем: и метаданными, и файлами.
* `DROP TABLE` = Удаление файлов.
* Расположение: По умолчанию в `spark.sql.warehouse.dir`.

## 2. External Table (Внешняя)
* Spark управляет только метаданными (схемой).
* `DROP TABLE` = Удаление только ссылки. Файлы в безопасности.
* Расположение: Указывается через `LOCATION`.

## 3. Best Practice
* Используйте **External Tables** для долговременного хранения (Data Lake).
* Используйте **Managed Tables** для временных расчетов внутри пайплайна.

## 4. Команды
* `CREATE DATABASE db_name`
* `USE db_name`
* `DESCRIBE EXTENDED table_name` — самая важная команда для отладки.
