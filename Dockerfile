FROM    python:3.7-alpine3.8

COPY    server /server
COPY    client /client

WORKDIR /client

RUN     apk --no-cache add sqlite nodejs nodejs-npm && \
        npm install ajv && \
        npm install && \
        npm run build && \
        rm -rf /client

WORKDIR /server

RUN     pip3 install -r requirements.txt

CMD     ["gunicorn", "testdataserver:app", "-b", "0.0.0.0:8000"]
