# 1st Stage
FROM python:3.10.12 as build-stage
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 90
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

