"""This module contains the ZipCodeAttribute class"""
import re
from uc3m_logistics.order_management_exception import OrderManagementException
from .attribute import Attribute

class OrderIdAttribute(Attribute):
    """Class for validating a zip_code"""
    def __init__(self):
        pass
    def validate(self, orderid):
        """Method for checking the order_id format"""
        try:
            my_order_id_re = re.compile(r"[0-9a-fA-F]{32}$")
            if not my_order_id_re.fullmatch(orderid):
                raise OrderManagementException("order id is not valid")
        except KeyError as ex:
            raise OrderManagementException("Bad label") from ex
        return orderid

    @property
    def data(self):
        """method for getting a phone_number"""
        return self._value

    @data.setter
    def data(self, value):
        """method for setting a phone_number"""
        self._value = self.validate(value)
