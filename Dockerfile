FROM    python:3.7-alpine3.8

COPY    server /server
COPY    client /client

WORKDIR /client

RUN     apk add sqlite nodejs nodejs-npm
RUN     npm install ajv 
RUN     npm install 
RUN     npm run build

RUN     rm -rf /client

WORKDIR /server

RUN     pip3 install -r requirements.txt

CMD     ["gunicorn", "testdataserver:app", "-b", "0.0.0.0:8000"]
