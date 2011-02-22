from optparse import make_option
from django.core.management.base import BaseCommand



class Command(BaseCommand):

    help = "Import the old data from the 'export' database unless database is specified with --database"

    def handle(self, *args, **options):
        """
        TODO: Add some options to manage this
        """
        db = 'export'
        
        print 'Importing data from:', db
