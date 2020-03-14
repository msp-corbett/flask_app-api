from app.backend.api.resource.base_api import BaseAPI
from .model import Widget_X

class WidgetXAPI(BaseAPI):

    def __init__(self):
        super().__init__()
        self.db_model = Widget_X