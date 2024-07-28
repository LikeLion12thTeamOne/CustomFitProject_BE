from django.core.management.base import BaseCommand
from customFit.db_uploader import load_csv_to_db

class Command(BaseCommand):
    help = 'Load CSV data into the database'

    def handle(self, *args, **kwargs):
        load_csv_to_db()
        self.stdout.write(self.style.SUCCESS('Successfully loaded CSV data'))