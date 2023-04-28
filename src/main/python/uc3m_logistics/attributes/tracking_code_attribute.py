"""This module contains the ZipCodeAttribute class"""
import re
from uc3m_logistics.order_management_exception import OrderManagementException
from uc3m_logistics.attributes.attribute import Attribute
from uc3m_logistics.exception_messages import ExceptionMessage


class TrackingCodeAttribute(Attribute):
    """Class for validating the tracking code"""
    def __init__(self):
        self._value = None
    # pylint: disable=arguments-renamed

    def validate(self, validate):
        """Method for checking the email format"""
        my_tracking_code = re.compile(r"[0-9a-fA-F]{64}$")
        if not my_tracking_code.fullmatch(validate):
            raise OrderManagementException(ExceptionMessage.TRACKING_CODE_NOT_VALID.value)
        return validate

    @property
    def data(self):
        """method for getting a phone_number"""
        return self._value

    @data.setter
    def data(self, value):
        """method for setting a phone_number"""
        self._value = self.validate(value)
