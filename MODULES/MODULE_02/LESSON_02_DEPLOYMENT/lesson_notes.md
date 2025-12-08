# Конспект: Режимы Развертывания

## 1. Режимы
* **Client Mode:** Driver на клиенте. Зависит от стабильности соединения. Для Dev/Interactive.
* **Cluster Mode:** Driver в кластере. Автономный. Для Production.

## 2. Cluster Managers
* **Local:** Одна машина (Dev).
* **YARN/K8s:** Распределенный кластер (Prod).

## 3. spark-submit
Главный инструмент запуска.
Пример:
spark-submit \
  --master yarn \
  --deploy-mode cluster \
  --conf spark.executor.memory=4g \
  my_script.py
