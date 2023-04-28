"""This module contains the ZipCodeAttribute class"""
from uc3m_logistics.order_management_exception import OrderManagementException
from uc3m_logistics.attributes.attribute import Attribute

class ZipCodeAttribute(Attribute):
    """Class for validating a zip_code"""
    def __init__(self):
        pass

    # pylint: disable=arguments-renamed
    def validate(self, zip_code):
        """method for validating a zip_code"""
        if zip_code.isnumeric() and len(zip_code) == 5:
            if (int(zip_code) > 52999 or int(zip_code) < 1000):
                raise OrderManagementException("zip_code is not valid")
        else:
            raise OrderManagementException("zip_code format is not valid")
        return zip_code

    @property
    def data(self):
        """method for getting a phone_number"""
        return self._value

    @data.setter
    def data(self, value):
        """method for setting a phone_number"""
        self._value = self.validate(value)
