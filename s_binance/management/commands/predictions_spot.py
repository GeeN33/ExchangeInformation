from django.core.management.base import BaseCommand, CommandError
from f_binance.tasks import task_go_prediction_5_new
from service.predicted import go_prediction


class Command(BaseCommand):
    help = 'predictions_spot'

    def handle(self, *args, **options):
        # task_go_prediction_5_new.delay()
        res = go_prediction('5')
        print(res)