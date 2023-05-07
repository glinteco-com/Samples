# Sample Flask App


## Installation guideline - Mac

### Pre-requisite packages

* Redis server
* pyenv
* pip
* postgreSQL

### Clone the repository

```
git clone https://github.com/glinteco-com/Samples
cd samples/flask_app
```

### Setup virtualenv

```
pyenv virtualenv 3.11.0 samples
pyenv activate samples
pip install -r requirements.txt
```

### Create database

```
psql postgres
```

then create user, database as follows

```
DROP DATABASE IF EXISTS samples;

CREATE DATABASE samples;

CREATE ROLE samples WITH LOGIN PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE samples TO samples;
```

then apply the new migration

```
flask db upgrade
```

### Run the app

```
flask run
```

and open the url 127.0.0.1:5000


### Run the celery

Open a new terminal tab and run the following command to run celery workers

```
celery -A celery_tasks worker -l info  # run celery workers
celery -A celery_tasks worker -B -l info  # run beat workers
```

### Run tests

```
pytest
```
