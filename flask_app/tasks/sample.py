from celery import shared_task


@shared_task()
def add_numbers(number1, number2):
    return number1 + number2
