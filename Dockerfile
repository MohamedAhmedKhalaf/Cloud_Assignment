FROM python:alpine

WORKDIR /application

COPY requirements.txt .

COPY paragraphs.txt .


RUN pip install -r requirements.txt

COPY app.py  .

CMD python app.py
