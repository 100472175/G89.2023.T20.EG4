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

# NEW IMPORTS
from uc3m_logistics.stores.order_request_store import OrderRequestStore
from uc3m_logistics.stores.order_shipping_store import OrderShippingStore
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
        """NEW PART"""
        #my_store = OrderRequestStore()
        #return my_store.find_item_by_key(my_order)


    # pylint: disable=too-many-locals
    def send_product(self, input_file):
        """Sends the order included in the input_file"""
        # New class
        data = SendProductInput.from_json(input_file)
        SendProductInput(orderId=data["OrderID"], email=data["ContactEmail"])

        my_store = OrderRequestStore()
        proid,reg_type = my_store.find_item_by_key(data["OrderID"])
        my_sign = OrderShipping(product_id=proid,
                                order_id=data["OrderID"],
                                order_type=reg_type,
                                delivery_email=data["ContactEmail"])
        """OLD
        my_store = Stores()
        my_store.robust_order_shipping_saving(my_sign)
        return my_sign.tracking_code
        """
        # NEW
        my_store = OrderShippingStore()
        my_store.add_item(my_sign)
        return my_sign.tracking_code


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
