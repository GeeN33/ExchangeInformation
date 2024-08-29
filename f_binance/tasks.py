from celery import shared_task

from core.celery import app
from f_binance.service import fetch_binance_data
from service.predicted import go_prediction
from service.telegram import send_mass_tg


@shared_task
def task_tg_test():
    send_mass_tg('test ok')

    return 'ok'

@shared_task
def task_binance_data():
    res = fetch_binance_data()

    return res

@shared_task
def task_go_prediction_5():
    res = go_prediction('5')

    return res

@shared_task
def task_go_prediction_60():
    res = go_prediction('60')

    return res

@app.task
def task_go_prediction_5_new():
    res = go_prediction('5')

    return res

# f_binance.tasks.task_go_prediction_5