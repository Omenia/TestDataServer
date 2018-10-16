# Test data server, with properties #

* Light-weight (web?) server with minimal dependecies
* Dynamic data allocation: No need to know, how many users are using the same pool, no need to manually divide the pool: User always gets the "oldest" data globally.
* Dynamic data allocation#2: All data is used (=global round robin), minimizes the need of the test data.
* Serves test data globally for the whole organisation (=guaranteed unique data)
* First Basic functionality: "Give me data". Which retrieves the first line and puts it last (round-robin)


* Client needing globally unique test data sends request to server. Request is basic http GET and response can be plain-text
* Server have to take care of race condition, simultaneous requests are queued and they are served as soon as earlier request is served and database unlocked
* Database can be file, file based DB, real DB...as long as it serves "light-weight"
* Possibility to expand later
  * Different test data/tables can live in their own ports.
  * Other fetching methods (give me random row. Push fetched row to the end=true/false, etc...
  * Set test data (row) locked until it is exclusively unlocked
  * Import data with UI and/or via API
* Implementation preferably with Python, release via Pypi, automated deployment pipeline (including tests), ....
* Source code hosted in Github
* Planned first (pre)release 0.0.1 available in Pypi @1.11.2018

## Running ##

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 server.py
```

## API documentation ##

Go to `localhost:5000/ui` when server is running.
