# Step 1

clone this repo

# Step 2

cd spark
`mkdir ./resources/photos`
`mkdir ./resources/processed`

# Step 3

run following commands in a terminal

`docker build --no-cache  --progress=plain  -t tiw-spark:3.0 .`

`docker-compose up`

# Step 4

wait for 30 minutes until all images will appear in ./resources/photos
and csv files will appear in ./resources/processed/processed

If you want to run Spark again, delete only processed dir and remove images
`rm -r ./resources/processed/processed`
`rm -r ./resources/photos`
`mkdir ./resources/photos`
