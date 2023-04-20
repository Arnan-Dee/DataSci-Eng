!/bin/bash

py -m venv spark
cd spark
.\spark\Scripts\activate
py -m pip install requests
py -m pip install pyspark==3.3.2 request pandas


docker-compose up --scale spark-worker=3
pip install pyspark