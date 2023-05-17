FROM apache/spark-py:v3.3.2 

USER root

RUN mkdir -p /mount_volumn && \
    apt-get install -y wget

WORKDIR /mount_volumn

RUN mkdir ./execution_scripts && \
    mkdir ./resources && \
    mkdir ./resources/photos && \
    mkdir ./resources/processed_files && \
    pip install --user requests && \
    wget -O /mount_volumn/resources/bangkok_traffy.csv https://publicapi.traffy.in.th/dump-csv-chadchart/bangkok_traffy.csv && \
    ls /mount_volumn/resources && \
    head -10 /mount_volumn/resources/bangkok_traffy.csv

COPY ./execution_scripts /mount_volumn/execution_scripts

CMD ["/opt/spark/bin/spark-submit", "/mount_volumn/execution_scripts/process.py"]




