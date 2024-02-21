FROM python:3.12.1-bookworm

RUN mkdir -p /home/app

RUN cd /home/app

COPY translate_fruit.py /home/app

COPY fruits_unicode.py /home/app

RUN pip3 install bottle

CMD ["python3", "/home/app/translate_fruit.py"]

