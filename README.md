# FastApi Docker

## Process Flows:

We show graphically the different processes of the mixer

![](images/app_flow.png)

## Requirements Virtual Environment:

1. Install virtual environment:
    pip3 install virtualenv
2. Create a virtual environment:
    python3 -m venv venv
3. Activate virtual environment:
    source venv/bin/activate
    
## Requirements to Create FastApi Docker image:

1. Go to directory when Dockerfile is situated
2. run **docker build -t fastapi .**
3. run uvicorn app.main:app --host "0.0.0.0" --port "8080"

## Requirements to Create Elastisearch and Kibana Docker image:

1. Go to directory when docker-compose.yml is situated.
2. run docker-compose up -d
3. Elasticsearch runs **http://localhost:9200**
4. Kibana runs **http://localhost:5601/app/kibana#/home**