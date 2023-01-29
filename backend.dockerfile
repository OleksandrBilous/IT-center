FROM python:3.11-buster

RUN mkdir /code
WORKDIR /code
ENV PYTHONPATH "${PYTHONPATH}/code"

COPY ./requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY ./ /code/

CMD ["python3", "app.py"]