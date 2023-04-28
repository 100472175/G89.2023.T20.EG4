"""This module contains the ZipCodeAttribute class"""
import re
from uc3m_logistics.order_management_exception import OrderManagementException
from uc3m_logistics.attributes.attribute import Attribute
from uc3m_logistics.exception_messages import ExceptionMessage


class EmailAttribute(Attribute):
    """Class for validating a email"""
    def __init__(self):
        self._value = None

    # pylint: disable=arguments-renamed
    def validate(self, email):
        """Method for checking the email format"""
        try:
            regex_email = r'^[a-z0-9]+([\._]?[a-z0-9]+)+[@](\w+[.])+\w{2,3}$'
            my_email_re = re.compile(regex_email)
            if not my_email_re.fullmatch(email):
                raise OrderManagementException(ExceptionMessage.EMAIL_NOT_VALID.value)
            return email
        except KeyError as ex:
            raise OrderManagementException("Bad label") from ex

    @property
    def data(self):
        """method for getting a phone_number"""
        return self._value

    @data.setter
    def data(self, value):
        """method for setting a phone_number"""
        self._value = self.validate(value)
