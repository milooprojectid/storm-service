FROM python:3.6-slim

WORKDIR /app

COPY ./main.py /app
COPY ./requirements.txt /app
COPY ./.env /app
COPY ./modules /app/modules

RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt

ENTRYPOINT ["python"]
CMD ["main.py"]
