"""
Commands that will wait for the db
"""
import time
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **kwargs):
        """Entrypoint for command."""
        self.stdout.write("Waiting for database...")
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (OperationalError, Psycopg2OpError):
                self.stdout.write("Database is not available yet.")
                time.sleep(1)
        self.stdout.write("Database is ready.")
