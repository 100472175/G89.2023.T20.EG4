"""Module """
import datetime
from datetime import datetime
from freezegun import freeze_time
from uc3m_logistics.stores.jsons_manager import JSON
from uc3m_logistics.stores.stores import Stores
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException
from .order_shipping import OrderShipping
from .order_manager_config import JSON_FILES_PATH
from .send_product_input import SendProductInput
from .order_delivery import OrderDelivery

class OrderManager:
    """Class for providing the methods for managing the orders process"""
    def __init__(self):
        self.__my_json = JSON()
        self.__my_store = Stores()

    # pylint: disable=too-many-arguments
    def register_order(self, product_id,
                       order_type,
                       address,
                       phone_number,
                       zip_code):
        """Register the orders into the order's file"""

        my_order = OrderRequest(product_id=product_id,
                                order_type=order_type,
                                delivery_address=address,
                                phone_number=phone_number,
                                zip_code=zip_code)

        self.__my_store.robust_saving(my_order)

        return my_order.order_id

    # pylint: disable=too-many-locals
    def send_product(self, input_file):
        """Sends the order included in the input_file"""

        """
        # check all the information
        self.check_order_id(data)
        self.check_email(data)
        """
        # New class
        data = SendProductInput.from_json(input_file)
        SendProductInput(orderId=data["OrderID"], email=data["ContactEmail"])
        file_store = JSON_FILES_PATH + "orders_store.json"
        data_list = self.__my_json.read_json_register_order(file_store)
        found = False
        found, proid, reg_type = self.order_object_generator(data, data_list, found)

        if not found:
            raise OrderManagementException("order_id not found")

        my_sign = OrderShipping(product_id=proid,
                                order_id=data["OrderID"],
                                order_type=reg_type,
                                delivery_email=data["ContactEmail"])

        my_store = Stores()
        my_store.robust_order_shipping_saving(my_sign)

        return my_sign.tracking_code

    def order_object_generator(self, data, data_list, found):
        """Generates the order object"""
        for item in data_list:
            if item["_OrderRequest__order_id"] == data["OrderID"]:
                found = True
                # retrieve the orders data
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

                if order.order_id != data["OrderID"]:
                    raise OrderManagementException("Orders' data have been manipulated")
        return found, proid, reg_type

    def deliver_product(self, tracking_code):
        """Register the delivery of the product"""
        my_order_delivery = OrderDelivery(tracking_code)
        return my_order_delivery.save_to_store()




"""
SINGLETON
    class __Singleton:
        def __init__(self):
            self.name = None

        def __str__(self):
            return 'self ' + str(self.name)

    instance = None

    def __new__(cls):
        if not OrderManager.instance:
            OrderManager.instance = OrderManager.__Singleton()

    def __getattr__(self, nombre):
        return getattr(self.instance, nombre)

    def __setattr__(self, nombre, valor):
        return setattr(self.instance, nombre, valor)

    return OrderManager.instance
"""
