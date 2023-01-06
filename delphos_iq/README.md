# To Run the project

## Postgres database
Start the database container

```shell
docker-compose run -d --service-ports --name psql psql
```

connect to the postgres container 

```shell
docker exec -it psql bash
```

create database name `delphos_iq`

## Backend Service

Once the project is clone, 
move to the project directory and run the following command:

build the backend service
```shell
docker-compose build backend 
```


```shell
docker-compose run --service-ports -d --name backend backend 
```

connect to the backend service and create migration files

```shell
docker exec -it CONTAINER_NAME bash
```
In the container run the following command

```shell
cd ..
python manage.py makemigrations
python manage.py migrate
```

## Run the scraper

The scraper can be run on your local machine after installing all the libraries

```shell
pip install -r requirements.txt
cd web_scraper
python main.py
```
once finish running the result file will be created in 

```shell
web_scraper/browser/result.csv
```
