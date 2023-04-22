"""Contains the class OrderDelivery"""
from datetime import datetime
from uc3m_logistics.stores.jsons_manager import JSON
from uc3m_logistics.attributes.tracking_code_attribute import TrackingCodeAttribute
from .order_manager_config import JSON_FILES_PATH
from .order_management_exception import OrderManagementException
# pylint: disable=too-many-instance-attributes
class OrderDelivery():
    """Class representing the shipping of an order"""

    def __init__(self, tracking_code):
        self.__tracking_code = TrackingCodeAttribute().validate(tracking_code)
        self.__my_json = JSON()
    @property
    def tracking_code(self):
        return self.__tracking_code
    @tracking_code.setter
    def tracking_code(self,value):
        self.__tracking_code = TrackingCodeAttribute().validate(value)

    def save_to_store(self):
        # check if this tracking_code is in shipments_store
        shimpents_store_file = JSON_FILES_PATH + "shipments_store.json"
        # first read the file
        data_list = self.__my_json.read_json_deliver_product(shimpents_store_file)
        # search this tracking_code
        found = False
        for item in data_list:
            if item["_OrderShipping__tracking_code"] == self.__tracking_code:
                found = True
                del_timestamp = item["_OrderShipping__delivery_day"]
        if not found:
            raise OrderManagementException("tracking_code is not found")

        today = datetime.today().date()
        delivery_date = datetime.fromtimestamp(del_timestamp).date()
        if delivery_date != today:
            raise OrderManagementException("Today is not the delivery date")

        shipments_file = JSON_FILES_PATH + "shipments_delivered.json"

        data_list = self.__my_json.read_json_register_order(shipments_file)

        # append the delivery info
        data_list.append(str(self.__tracking_code))
        data_list.append(str(datetime.utcnow()))
        return self.__my_json.write_json(shipments_file, data_list)