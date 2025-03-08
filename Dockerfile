FROM python:3.12

RUN apt update -y 

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "-B", "app.py"]