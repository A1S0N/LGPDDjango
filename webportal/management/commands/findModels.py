from webportal.management.sqlite.conSqlite3 import getFields, getModels
from django.core.management.base import BaseCommand

class Command(BaseCommand):
  help = 'Find models from DB'

  def handle(self, *args, **options):
    print('\n[*] Getting Data...\n')
    print(f'Models: {getModels()}\n')
    print(f'Fields: {getFields(getModels())}\n')