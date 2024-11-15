from celery import app

@app.shared_task
def calculate_birth_year(age):
    return 2024 - age