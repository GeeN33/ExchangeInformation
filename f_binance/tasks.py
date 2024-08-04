from celery import shared_task

from f_binance.service import fetch_binance_data
from service.predicted import go_prediction


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


# f_binance.tasks.task_binance_data