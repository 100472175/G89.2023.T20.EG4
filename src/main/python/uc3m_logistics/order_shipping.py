"""Contains the class OrderShipping"""
from datetime import datetime
import hashlib
from uc3m_logistics.attributes.product_id_attribute import ProductIdAttribute
from .order_management_exception import OrderManagementException
from uc3m_logistics.attributes.tracking_code_attribute import TrackingCodeAttribute
from uc3m_logistics.stores.order_shipping_store import OrderShippingStore

# pylint: disable=too-many-instance-attributes
class OrderShipping():
    """Class representing the shipping of an order"""

    def __init__(self, product_id, order_id, delivery_email, order_type):
        self.__alg = "SHA-256"
        self.__type = "DS"
        self.product_id = product_id
        self.order_id = order_id
        self.delivery_email = delivery_email
        justnow = datetime.utcnow()
        self.__issued_at = datetime.timestamp(justnow)
        if order_type == "Regular":
            delivery_days = 7
        else:
            delivery_days = 1
        # timestamp is represneted in seconds.microseconds
        # __delivery_day must be expressed in senconds to be added to the timestap
        self.__delivery_day = self.__issued_at + (delivery_days * 24 * 60 * 60)
        self.__tracking_code = hashlib.sha256(self.__signature_string().encode()).hexdigest()

    def __signature_string(self):
        """Composes the string to be used for generating the tracking_code"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",order_id:" + \
            self.__order_id + ",issuedate:" + str(self.__issued_at) + \
            ",deliveryday:" + str(self.__delivery_day) + "}"
    """
    def save_to_store(self):
        OrderRequestStore().add_item(self)
    """
    def from_tracking_code(self,tracking_code:str):
        TrackingCodeAttribute().validate(tracking_code)
        order_shipping = OrderShippingStore().find_item_by_key(tracking_code)
        if not order_shipping:
            raise OrderManagementException("tracking_code is not found")
        return order_shipping

    @property
    def product_id(self):
        """Property that represents the product_id of the order"""
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = ProductIdAttribute().validate(value)

    @property
    def order_id(self):
        """Property that represents the order_id"""
        return self.__order_id

    @order_id.setter
    def order_id(self, value):
        self.__order_id =value

    @property
    def email(self):
        """Property that represents the email of the client"""
        return self.__delivery_email

    @email.setter
    def email(self, value):
        self.__delivery_email = value

    @property
    def tracking_code(self):
        """returns the tracking code"""
        return self.__tracking_code

    @property
    def issued_at(self):
        """Returns the issued at value"""
        return self.__issued_at

    @issued_at.setter
    def issued_at(self, value):
        self.__issued_at = value

    @property
    def delivery_day(self):
        """Returns the delivery day for the order"""
        return self.__delivery_day
