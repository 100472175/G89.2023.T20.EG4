"""Module for validating a order_type"""
import json
from abc import ABC, abstractmethod
from uc3m_logistics.order_management_exception import OrderManagementException
from uc3m_logistics.exception_messages import ExceptionMessage

class JsonStore(ABC):
    """Class for reading and writing json files"""
    _FILE_PATH = ""
    def __init__(self):
        self.__data = self.load()

    def load(self):
        """Method for loading a json file"""
        try:
            with open(self._FILE_PATH, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
            with open(self._FILE_PATH, "w", encoding="utf-8", newline="") as file:
                json.dump(data, file, indent=2)
        except json.JSONDecodeError as ex:
            raise OrderManagementException(ExceptionMessage.JSON_DECODE_ERROR.value) from ex
        return data

    def save(self):
        """Method for saving a json file"""
        try:
            with open(self._FILE_PATH, "w", encoding="utf-8", newline="") as file:
                json.dump(self.__data, file, indent=2)
        except FileNotFoundError as exc:
            raise OrderManagementException(ExceptionMessage.WRONG_FILE_OR_PATH.value) from exc

    @abstractmethod
    def find_item_by_key(self, key):
        """Method for finding an item by key"""

    @abstractmethod
    def add_item(self, new_item):
        """Method for adding an item"""

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
        self.save()
