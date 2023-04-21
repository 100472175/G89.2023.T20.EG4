"""Contains the class OrderDelivery"""
from datetime import datetime
import hashlib
from uc3m_logistics.attributes.product_id_attribute import ProductIdAttribute
from .order_management_exception import OrderManagementException
from uc3m_logistics.attributes.tracking_code_attribute import TrackingCodeAttribute
from uc3m_logistics.stores.order_shipping_store import OrderShippingStore

# pylint: disable=too-many-instance-attributes
class OrderShipping():
    """Class representing the shipping of an order"""

    def __init__(self, tracking_code):
        self.__tracking_code = TrackingCodeAttribute().validate(tracking_code)
    @property
    def tracking_code(self):
        return self.__tracking_code
    @tracking_code.setter
    def tracking_code(self,value):
        self.__tracking_code = TrackingCodeAttribute().validate(value)

    def save_to_store(self):
        pass