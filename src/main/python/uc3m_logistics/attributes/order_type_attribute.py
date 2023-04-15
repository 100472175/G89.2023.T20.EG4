"""Module for validating a order_type"""
import re
from uc3m_logistics.attributes.attribute import Attribute
from uc3m_logistics.order_management_exception import OrderManagementException


class OrderTypeAttribute(Attribute):
    """Class for validating a order_type"""
    def __init__(self):
        pass

    def validate(self, value):
        """method for validating a order_type"""
        my_order_type_re = re.compile(r"(Regular|Premium)")
        if not my_order_type_re.fullmatch(value):
            raise OrderManagementException("order_type is not valid")
        return value

    @property
    def data(self):
        """method for getting a phone_number"""
        return self._value

    @data.setter
    def data(self, value):
        """method for setting a phone_number"""
        self._value = self.validate(value)
