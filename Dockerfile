FROM python:3.9
LABEL mantainer="renatohk10@gmail.com"

WORKDIR /app

COPY . .


RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/sh","/app/entrypoint.sh"]