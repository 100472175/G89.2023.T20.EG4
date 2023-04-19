"""Module """
import datetime
import re
from datetime import datetime
from freezegun import freeze_time
from uc3m_logistics.stores.jsons_manager import JSON
from uc3m_logistics.stores.stores import Stores
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException
from .order_shipping import OrderShipping
from .order_manager_config import JSON_FILES_PATH
from .send_product_input import SendProductInput

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

    def check_email(self, data):
        """Method for checking the email format"""
        try:
            regex_email = r'^[a-z0-9]+([\._]?[a-z0-9]+)+[@](\w+[.])+\w{2,3}$'
            my_email_re = re.compile(regex_email)
            if not my_email_re.fullmatch(data["ContactEmail"]):
                raise OrderManagementException("contact email is not valid")
        except KeyError as ex:
            raise OrderManagementException("Bad label") from ex

    def check_order_id(self, data):
        """Method for checking the order_id format"""
        try:
            my_order_id_re = re.compile(r"[0-9a-fA-F]{32}$")
            if not my_order_id_re.fullmatch(data["OrderID"]):
                raise OrderManagementException("order id is not valid")
        except KeyError as ex:
            raise OrderManagementException("Bad label") from ex

    @staticmethod
    def validate_tracking_code(t_c):
        """Method for validating sha256 values"""
        my_tracking_code = re.compile(r"[0-9a-fA-F]{64}$")
        if not my_tracking_code.fullmatch(t_c):
            raise OrderManagementException("tracking_code format is not valid")

    def deliver_product(self, tracking_code):
        """Register the delivery of the product"""
        self.validate_tracking_code(tracking_code)

        # check if this tracking_code is in shipments_store
        shimpents_store_file = JSON_FILES_PATH + "shipments_store.json"
        # first read the file
        data_list = self.__my_json.read_json_deliver_product(shimpents_store_file)
        # search this tracking_code
        self.get_tracking_code_datetime(data_list, tracking_code)

        shipments_file = JSON_FILES_PATH + "shipments_delivered.json"

        data_list = self.__my_json.read_json_register_order(shipments_file)

            # append the delivery info
        data_list.append(str(tracking_code))
        data_list.append(str(datetime.utcnow()))
        return self.__my_json.write_json(shipments_file,data_list)

    def get_tracking_code_datetime(self, data_list, tracking_code):
        """Method for getting the tracking code and the datetime"""
        found = False
        for item in data_list:
            if item["_OrderShipping__tracking_code"] == tracking_code:
                found = True
                del_timestamp = item["_OrderShipping__delivery_day"]
        if not found:
            raise OrderManagementException("tracking_code is not found")

        today = datetime.today().date()
        delivery_date = datetime.fromtimestamp(del_timestamp).date()
        if delivery_date != today:
            raise OrderManagementException("Today is not the delivery date")


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
