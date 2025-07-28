FROM python:3.12

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN python init_db.py

CMD ["python", "app/app.py"]
