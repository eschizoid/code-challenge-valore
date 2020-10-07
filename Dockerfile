FROM python:3.8

WORKDIR /code
COPY data/shakespeare.txt .
COPY requirements.txt .
COPY src/ .

RUN pip install -r requirements.txt

CMD [ "python", "./driver.py" ]
