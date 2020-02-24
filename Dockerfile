FROM python:3.6-slim

WORKDIR /app

COPY ./main.py /app
COPY ./requirements.txt /app
COPY ./.env /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["main.py"]
