"""Module in charge of order_resuests' data management"""
from datetime import datetime
from freezegun import freeze_time
from uc3m_logistics.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.order_management_exception import OrderManagementException
from uc3m_logistics.stores.jsons_store import JsonStore
from uc3m_logistics.order_request import OrderRequest
from uc3m_logistics.exception_messages import ExceptionMessage


class OrderRequestStore:
    """Class in charge of order_resuests' data management"""
    class __OrderRequestStore(JsonStore):
        _FILE_PATH = JSON_FILES_PATH + "orders_store.json"

        def find_item_by_key(self, key: str):
            self.data = self.load()
            found_item = False
            item = None
            for order in self.data:
                if order["_OrderRequest__order_id"] == key:
                    found_item = True
                    item = order
            if found_item:
                proid = item["_OrderRequest__product_id"]
                address = item["_OrderRequest__delivery_address"]
                reg_type = item["_OrderRequest__order_type"]
                phone = item["_OrderRequest__phone_number"]
                order_timestamp = item["_OrderRequest__time_stamp"]
                zip_code = item["_OrderRequest__zip_code"]
                # set the time when the order was registered for checking the md5
                with freeze_time(datetime.fromtimestamp(order_timestamp).date()):
                    order = OrderRequest(product_id=proid,
                                         delivery_address=address,
                                         order_type=reg_type,
                                         phone_number=phone,
                                         zip_code=zip_code)
                if order.order_id != key:
                    raise OrderManagementException(ExceptionMessage.ORDERS_DATA_MANIPULATED.value)
                return proid, reg_type
            raise OrderManagementException(ExceptionMessage.ORDER_ID_NOT_FOUND.value)

        def add_item(self, new_item):
            self.data = self.load()
            found = False
            for item in self.data:
                if item["_OrderRequest__order_id"] == new_item.order_id:
                    found = True
            if not found:
                self.data.append(new_item.__dict__)
            else:
                raise OrderManagementException(ExceptionMessage.ORDER_ID_ALREADY_REGISTERED.value)
            self.save()

    instance = None

    def __new__(cls):
        if not OrderRequestStore.instance:
            OrderRequestStore.instance = OrderRequestStore.__OrderRequestStore()
        return OrderRequestStore.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)

    def __init__(self):
        pass
