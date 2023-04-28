# Oveview
 
&nbsp;&nbsp;&nbsp;&nbsp;This project is a project to do a simple ETL. This project include these tech:

1. Python programming language
2. Docker
3. PostgreSQL

- [data dir](/data): contains all the data that is already downloaded from kaggel [Global Energy Statistics - Kaggle](https://www.kaggle.com/datasets/akhiljethwa/world-energy-statistics)
- [etl dir](/etl): contains all python scripts that is used to do ETL

# How To Use

1. Clone this repository
2. Pull postgres image from docker using this command line ```docker pull postgres```
3. Run docker images using this command 
```
docker run -d 
    --name simple_etl
    -p 5434:5432
    -e POSTGRES_PASSWORD=[your password]
    postgres
```
4. Run this to access PostgreSQL from command line ```docker exec -it simple_etl psql -U postgres```
5. Create database using this command ```create database energy_consumption;```
6. Go to [etl dir](/etl) and run ```python load.py -f [file path]```
7. Then ETL process will completed 👍👨🏻‍💻