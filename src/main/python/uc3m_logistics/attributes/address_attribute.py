"""Module for AddressAttribute class"""
import re
from uc3m_logistics.order_management_exception import OrderManagementException
from uc3m_logistics.attributes.attribute import Attribute
from uc3m_logistics.exception_messages import ExceptionMessage


class AddressAttribute(Attribute):
    """Class for validating a address"""
    def __init__(self):
        self._value = None

    def validate(self, value):
        """method for validating a address"""
        my_address_re = re.compile(r"^(?=^.{20,100}$)(([a-zA-Z0-9]+\s)+[a-zA-Z0-9]+)$")
        if not my_address_re.fullmatch(value):
            raise OrderManagementException(ExceptionMessage.ADDRESS_NOT_VALID.value)
        return value

    @property
    def data(self):
        """method for getting a phone_number"""
        return self.value

    @data.setter
    def data(self, value):
        """method for setting a phone_number"""
        self._value = self.validate(value)
