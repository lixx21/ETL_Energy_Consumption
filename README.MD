# Oveview
 
&nbsp;&nbsp;&nbsp;&nbsp;This project is a project to do a simple ETL. This project include these tech:

1. Python programming language
2. Docker
3. PostgreSQL

- [data dir](/data): contains all the data that is already downloaded from kaggel [Global Energy Statistics - Kaggle](https://www.kaggle.com/datasets/akhiljethwa/world-energy-statistics)
- [etl dir](/etl): contains all python scripts that is used to do ETL

# How To Use

1. Clone this repository
2. Create volume name **etl_energy_consumption** with this command ```docker volume create etl_energy_consumption```
3. PostgreSQL using this path to save their data in docker */var/lib/postgresql/data*. Therefore if you want to use volume then the path of your volume will be like this ```[your volume name]:/var/lib/postgresql/data```. So the volume will be like this ```etl_energy_consumption:/var/lib/postgresql``` 
4. Pull postgres image from docker using this command line ```docker pull postgres```
5. create network for docker by using this command line ```docker network create energy_consumption_network```
6. Pull pgadmin in docker using this command line ```docker pull dpage/pgadmin4```
7. Run docker compose using this command line ```docker-compose up -d```

```
NOTE:
If you want to connect docker with network you cannot used localhost, but you have to see the IP of the connection using:

docker network inspect [network name]

Then you will see the IP of the connection

or you can just use name of the container to connect each container
```

**This is the image of your pgadmin connection**
![image](https://user-images.githubusercontent.com/91602612/235394901-99968fc3-db33-42a8-846e-fb6de8f6295d.png)


8. install pgcli to see your PostgreSQL from command line ```pip install pgcli```
9. Run this to access PostgreSQL from command line ```pgcli -h localhost -p 5432 -u postgres -d energy_consumption```
10. Build image for our etl script by running this command ```docker build -t python-etl .```
11. Go to [etl dir](/etl) and run 
```
docker run -it --network=energy_consumption_network python-etl -f [file-path] -db energy_consumption -hs localhost -u postgres -pass 123456 -p 5432
```
12. Then ETL process will completed 👍👨🏻‍💻
