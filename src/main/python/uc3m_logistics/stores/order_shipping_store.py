from uc3m_logistics.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.stores.jsons_store import JsonStore
class OrderShippingStore(JsonStore):
    _File_Path = JSON_FILES_PATH + "shipments_store.json"

    def find_item_by_key(self, key):
        print("OrderShippingStore find_item_by_key",key,self.data)
        for item in self.data:
            if item["_OrderShipping__tracking_code"] == key:
                return item
        return None
    def add_item(self,new_item):
        self.data.append(new_item.__dict__)
        self.save()

