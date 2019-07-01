FROM    python:3.7.2-stretch

RUN     apt-get update && apt-get install -yq firefox-esr

RUN     wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz" -O /tmp/geckodriver.tgz  \
    && tar zxf /tmp/geckodriver.tgz -C /usr/bin/ \
    && rm /tmp/geckodriver.tgz

COPY    . /robottests

WORKDIR /robottests

RUN     pip3 install -r requirements.txt

CMD     ["sh", "-c", "python3 -m robot -P . -d output --listener listeners/listener.py -v BASE_URL:$BASE_URL $ROBOT_OPTIONS ."]
