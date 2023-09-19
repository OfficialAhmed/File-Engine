"""
    Parent class holds constant values 
    for the interface
"""


class Constant:

    _RESOURCES_PATH = ":/images/images/"


    @classmethod
    def get_resources_path(self):
        return self._RESOURCES_PATH