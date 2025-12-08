#!/bin/bash

echo "Starting Job 1..."
/usr/local/spark/bin/spark-submit \
    --master local[2] \
    /home/jovyan/workspace/MODULES/MODULE_02/LESSON_02_DEPLOYMENT/production_app.py "Job1"

if [ $? -eq 0 ]; then
    echo "Job 1 success! Staring Job 2..."
    /usr/local/spark/bin/spark-submit \
    --master local[4] \
    /home/jovyan/workspace/MODULES/MODULE_02/LESSON_02_DEPLOYMENT/production_app.py "Job2"
else
    echo "Job 1 failed"
fi