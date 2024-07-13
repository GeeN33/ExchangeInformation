from celery import shared_task

from f_binance.service import fetch_binance_data


@shared_task
def task_binance_data():
    fetch_binance_data()