from django.apps import apps
from import_export.resources import modelresource_factory
#from celery.utils.log import get_task_logger
import logging

logger = logging.getLogger(__name__)

log = logging.getLogger('huey')



class ModelConfig:
    def __init__(self, app_label=None, model_name=None, resource=None):
        self.model = apps.get_model(app_label=app_label, model_name=model_name)
        log.debug(resource)
        if resource:
            self.resource = resource()
        else:
            self.resource = modelresource_factory(self.model)
