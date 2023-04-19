"""Stores class"""
import json
from uc3m_logistics.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.order_management_exception import OrderManagementException
from .jsons_manager import JSON

class Stores:
    """Stores class"""
    def __init__(self):
        pass

    @staticmethod
    def robust_saving(data):
        """Method for saving the orders store"""

        # Read the JSON
        file_store = JSON_FILES_PATH + "orders_store.json"
        my_json = JSON()
        data_list = my_json.read_json_register_order(file_store)

        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == data.order_id:
                found = True
        if not found:
            data_list.append(data.__dict__)
        else:
            raise OrderManagementException("order_id is already registered in orders_store")
        return my_json.write_json(file_store, data_list)

    @staticmethod
    def robust_order_shipping_saving(shipment):
        """Saves the shipping object into a file"""
        # Read the file
        shipments_store_file = JSON_FILES_PATH + "shipments_store.json"
        my_json = JSON()
        data_list = my_json.read_json_register_order(shipments_store_file)

        # append the shipments list
        data_list.append(shipment.__dict__)

        my_json.write_json(shipments_store_file, data_list)
