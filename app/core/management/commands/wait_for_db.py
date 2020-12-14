import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""
    def handle(self, *args, **options):
        self.stdout.write('Waiting for PostgresDB...')
        db_connected = None
        while not db_connected:
            try:
                db_connected = connections['default']
            except OperationalError:
                self.stdout.write('PostgresDB not up yet, waiting 1s...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('PostgresDB up!'))
