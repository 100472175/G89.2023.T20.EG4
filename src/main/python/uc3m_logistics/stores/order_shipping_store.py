"""Module that manages the shipments' data"""
from datetime import datetime
from uc3m_logistics.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.stores.jsons_store import JsonStore
from uc3m_logistics.order_management_exception import OrderManagementException
from uc3m_logistics.exception_messages import ExceptionMessage


class OrderShippingStore:
    """Class in charge of shipments' data management"""
    class __OrderShippingStore(JsonStore):
        _FILE_PATH = JSON_FILES_PATH + "shipments_store.json"

        def find_item_by_key(self, key):
            self.data = self.load()
            found = False
            del_timestamp = False
            for item in self.data:
                if item["_OrderShipping__tracking_code"] == key:
                    found = True
                    del_timestamp = item["_OrderShipping__delivery_day"]
            if not found:
                raise OrderManagementException(ExceptionMessage.TRACKING_CODE_NOT_FOUND.value)

            today = datetime.today().date()
            delivery_date = datetime.fromtimestamp(del_timestamp).date()
            if delivery_date != today:
                raise OrderManagementException(ExceptionMessage.DATE_NOT_VALID.value)
            return del_timestamp

        def add_item(self, new_item):
            self.data = self.load()
            self.data.append(new_item.__dict__)
            self.save()

    instance = None

    def __new__(cls):
        if not OrderShippingStore.instance:
            OrderShippingStore.instance = OrderShippingStore.__OrderShippingStore()
        return OrderShippingStore.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)

    def __init__(self):
        pass
