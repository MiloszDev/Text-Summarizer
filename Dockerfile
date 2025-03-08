FROM python:3.12

RUN apt update -y 

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "-B", "app.py"]