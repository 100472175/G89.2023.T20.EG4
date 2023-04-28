"""This module contains the OrderDeliveryStore class"""
from datetime import datetime
from uc3m_logistics.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.stores.jsons_store import JsonStore


class OrderDeliveryStore:
    """This class is a singleton that represents the store of the orders delivered"""
    class __OrderDeliveryStore(JsonStore):
        _FILE_PATH = JSON_FILES_PATH + "shipments_delivered.json"

        def add_item(self, new_item):
            """Method for adding an item"""
            order_delivered = {"_OrderDelivery": str(new_item), "Datetime": str(datetime.utcnow())}
            self.data.append(order_delivered)
            self.save()

        def find_item_by_key(self, key):
            """Necessary for the abstract class"""

    instance = None

    def __new__(cls):
        if not OrderDeliveryStore.instance:
            OrderDeliveryStore.instance = OrderDeliveryStore.__OrderDeliveryStore()
        return OrderDeliveryStore.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)

    def __init__(self):
        pass
