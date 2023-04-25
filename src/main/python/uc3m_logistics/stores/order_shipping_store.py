from uc3m_logistics.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.stores.jsons_store import JsonStore
from uc3m_logistics.order_management_exception import OrderManagementException
from datetime import datetime
class OrderShippingStore(JsonStore):
    _FILE_PATH = JSON_FILES_PATH + "shipments_store.json"

    def find_item_by_key(self, key):
        found = False
        del_timestamp = False
        for item in self.data:
            if item["_OrderShipping__tracking_code"] == key:
                found = True
                del_timestamp = item["_OrderShipping__delivery_day"]
        if not found:
            raise OrderManagementException("tracking_code is not found")

        today = datetime.today().date()
        delivery_date = datetime.fromtimestamp(del_timestamp).date()
        if delivery_date != today:
            raise OrderManagementException("Today is not the delivery date")
        #return del_timestamp
    def add_item(self,new_item):
        self.data.append(new_item.__dict__)
        self.save()

