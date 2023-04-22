"""Module for validating a order_type"""
import json
from abc import ABC,abstractmethod
from uc3m_logistics.order_management_exception import OrderManagementException


class JsonStore(ABC):
    """Class for reading and writing json files"""
    _FILE_PATH = ""
    def __init__(self):
        self.data = self.load()
    def load(self):
        try:
            with open(self._FILE_PATH,"r",encoding="utf-8",newline="") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
            with open(self._FILE_PATH,"w",encoding="utf-8",newline="") as file:
                json.dump(data,file,indent=2)
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return data
    def save(self):
        try:
            with open(self._File_PATH,"w",encoding="utf-8",newline="") as file:
                json.dump(self.__data,file,indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path")
    @abstractmethod
    def find_item_by_key(self,key):
        pass
    @abstractmethod
    def add_item(self,new_item):
        pass
    @property
    def data(self):
        return self.__data
"""
# Add_item in order_request_store.py
        found = False
        for item in self.data:
            if item["_OrderRequest__order_id"] == new_item.order_id:
                found = True
        if not found:
            self.data.append(new_item.__dict__)
        else:
            raise OrderManagementException("order_id is already registered in order request")
        self.save()
"""