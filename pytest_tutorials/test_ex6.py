# Write a fixture that sets up a database connection and closes it after each test.

import pytest
import sqlite3


@pytest.fixture(scope="module")
def db():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()


def test_query(db):
    cursor = db.cursor()
    cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test (id, name) VALUES (?, ?)", (1, "Alice"))
    cursor.execute("INSERT INTO test (id, name) VALUES (?, ?)", (2, "Bob"))
    db.commit()
    cursor.execute("SELECT * FROM test")
    results = cursor.fetchall()
    assert len(results) == 2
