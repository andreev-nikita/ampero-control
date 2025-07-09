#__init__.py
from .ampero_control import AmperoControl

def create_instance(c_instance):
    return AmperoControl(c_instance)