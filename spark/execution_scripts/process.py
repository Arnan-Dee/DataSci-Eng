import os
import requests
from operator import add
from pyspark.sql import SparkSession
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id
from pyspark.sql.functions import concat,col,lit

def download_image(row):
        photo_path = '/mount_volumn/resources/photos'
        img_url = row['photo']
        index = row['index']
        img_filename = f'{photo_path}/image_{index}.jpg'
        try: 
            response = requests.get(img_url)
            print("Got image from URL")
        except:
            print(img_url)
            print(index)
            return
        if response.status_code != 200:
            print("Got not 200")
            print(response.content)
            print(response.headers)
            return
        try: 
            with open(img_filename, 'wb') as destination_image:
                print(f"image name = {img_filename}")
                destination_image.write(response.content)
        except:
             print("IO error")



spark_url = 'local'
spark = SparkSession.builder\
    .master(spark_url)\
    .appName('Spark')\
    .getOrCreate()

path = '/mount_volumn/resources/bangkok_traffy.csv'
print(path)
df = spark.read.option("delimiter", ",").option("header", True).csv(path)
cols = [c.replace('.', '_') for c in df.columns]
df = df.toDF(*cols)
print("fetched csv")


df = df.filter("type == '{จราจร}'")
df_filter = df.na.drop()
df_append_col = df_filter.withColumn('index', monotonically_increasing_id())


df_test = df_append_col
df_test.show()
df_test.foreach(download_image)
print("downloading images")

df_filename = df_test.withColumn('filename', concat(lit('image_'), col('index'), lit('.jpg')))
df_final = df_filename

df_final.write.option("header",True).csv('/mount_volumn/resources/processed_files/processed')
print("Successfully create CSV in processed")








