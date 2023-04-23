from uc3m_logistics.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.order_management_exception import OrderManagementException
from uc3m_logistics.stores.jsons_store import JsonStore
from datetime import datetime
class OrderDeliveryStore(JsonStore):
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

    def add_item(self, t_c):
        self._FILE_PATH = JSON_FILES_PATH + "shipments_delivered.json"
        self.data.append(str(t_c))
        self.data.append(str(datetime.utcnow()))
        self.save()