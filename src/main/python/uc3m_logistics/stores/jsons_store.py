"""Module for validating a order_type"""
import json
from abc import abstractmethod
from uc3m_logistics.order_management_exception import OrderManagementException


class JSON:
    """Class for reading and writing json files"""
    def __init__(self):
        pass
    def load(self):
        pass
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