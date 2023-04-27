from uc3m_logistics.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.stores.jsons_store import JsonStore
from datetime import datetime


class OrderDeliveryStore():
    class __OrderDeliveryStore(JsonStore):
        _FILE_PATH = JSON_FILES_PATH + "shipments_delivered.json"

        def add_item(self, t_c):
            self.data.append(str(t_c))
            self.data.append(str(datetime.utcnow()))
            self.save()

        def find_item_by_key(self, key):
            pass

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
