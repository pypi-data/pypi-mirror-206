__all__ = ['Env']
import os
from dotenv import load_dotenv
from pathlib import PurePath


class Env:
    ROUTE_PATH_TEMPLATE = 'ROUTE_{}_PATH'
    ROUTE_TEXT_TEMPLATE = 'ROUTE_{}_PATH'
    BOOTSTRAP_CSS_TEMPLATE = 'BOOTSTRAP_CSS_{}'
    BOOTSTRAP_SCRIPT_TEMPLATE = 'BOOTSTRAP_SCRIPT_{}'
    STATIC_LOGO = 'STATIC_LOGO_{}'

    def __init__(self, env_path: PurePath = None):
        self.env_path = env_path
        load_dotenv(dotenv_path=self.env_path)

    @staticmethod
    def get(variable: str):
        return os.environ.get(variable.upper())
        
    def get_route_path(self, name: str):
        return self.get(self.ROUTE_PATH_TEMPLATE.format(name.upper()))
    
    def get_route_text(self, name: str):
        return self.get(self.ROUTE_TEXT_TEMPLATE.format(name.upper()))
    
    def get_route_tuple(self, name: str):
        return self.get_route_path(name), self.get_route_text(name)
    
    def static_logo_path(self):
        return self.get(self.STATIC_LOGO.format('PATH'))
    
    def static_logo_text(self):
        return self.get(self.STATIC_LOGO.format('TEXT'))
    