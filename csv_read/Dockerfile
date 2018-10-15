FROM python:3

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install -e .

EXPOSE 5000

CMD ["python","./csv_read/app.py"]