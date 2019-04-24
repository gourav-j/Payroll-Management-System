from django.apps import AppConfig

class PmsConfig(AppConfig):
    name = 'pms'

    def ready(self):
    	from . import updater
    	updater.start()