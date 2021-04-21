FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 8080

COPY ./app /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]