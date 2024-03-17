FROM python:3.12.2

WORKDIR /app

COPY . /app

CMD ["python", "your_script.py"]