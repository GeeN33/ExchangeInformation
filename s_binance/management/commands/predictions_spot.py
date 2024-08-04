from django.core.management.base import BaseCommand, CommandError

from service.predicted import go_prediction


class Command(BaseCommand):
    help = 'predictions_spot'

    def handle(self, *args, **options):
        go_prediction('5')