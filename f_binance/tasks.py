from celery import shared_task

from f_binance.service import fetch_binance_data

@shared_task
def task_binance_data():
    res = fetch_binance_data()

    return res



# f_binance.tasks.task_binance_data