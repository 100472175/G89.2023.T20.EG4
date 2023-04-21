"""This module contains the ZipCodeAttribute class"""
import re
from uc3m_logistics.order_management_exception import OrderManagementException
from .attribute import Attribute

class TrackingCodeAttribute(Attribute):
    """Class for validating a zip_code"""
    def __init__(self):
        pass
    def validate(self, t_c):
        """Method for checking the email format"""
        my_tracking_code = re.compile(r"[0-9a-fA-F]{64}$")
        if not my_tracking_code.fullmatch(t_c):
            raise OrderManagementException("tracking_code format is not valid")
        return t_c
    @property
    def data(self):
        """method for getting a phone_number"""
        return self._value

    @data.setter
    def data(self, value):
        """method for setting a phone_number"""
        self._value = self.validate(value)
