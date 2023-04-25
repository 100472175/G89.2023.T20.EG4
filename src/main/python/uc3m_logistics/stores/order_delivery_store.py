from uc3m_logistics.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.stores.jsons_store import JsonStore
from datetime import datetime
class OrderDeliveryStore(JsonStore):
    _FILE_PATH = JSON_FILES_PATH + "shipments_delivered.json"
    def find_item_by_key(self,key):
        pass
    def add_item(self, t_c):
        self.data.append(str(t_c))
        self.data.append(str(datetime.utcnow()))
        self.save()