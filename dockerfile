FROM python:3.8

#create working directory for this docker run scripts
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY etl/ /etl
COPY data/ /data

ENTRYPOINT ["python", "/etl/load.py"]