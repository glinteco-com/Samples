# A sample FastAPI application

Install required packages

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the test

```
pytest
```

Run the app

```
uvicorn main:app --reload
```

The app is running now. Open a new browser window with the url `http://127.0.0.1:8000/docs`, you will see an API documentation page.

We can test the api by opening a new terminal tab and run

```
curl --location 'http://127.0.0.1:8000/books/' \
--header 'Content-Type: application/json' \
--data '{
    "title": "book 1",
    "author": "Joe Vu",
    "price": 10.3
}'
```

We can open the url `http://127.0.0.1:8000/books/` to see the new books added. Or we can run the command bellow

```
curl --location 'http://127.0.0.1:8000/books/'
```
