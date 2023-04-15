"""This module contains the PhoneNumberAttribute class"""
import re
from uc3m_logistics.order_management_exception import OrderManagementException
from .attribute import Attribute

class PhoneNumberAttribute(Attribute):
    """Class for validating a phone_number"""
    def __init__(self):
        pass
    def validate(self, phone_number):
        """method for validating a phone_number"""
        my_phone_number_re = re.compile(r"^(\+)[0-9]{11}")
        if not my_phone_number_re.fullmatch(phone_number):
            raise OrderManagementException("phone number is not valid")
        return phone_number

    @property
    def data(self):
        """method for getting a phone_number"""
        return self._value

    @data.setter
    def data(self, value):
        """method for setting a phone_number"""
        self._value = self.validate(value)
