"""This module contains the ZipCodeAttribute class"""
import re
from uc3m_logistics.order_management_exception import OrderManagementException
from uc3m_logistics.attributes.attribute import Attribute
from uc3m_logistics.exception_messages import ExceptionMessage

class OrderIdAttribute(Attribute):
    """Class for validating the order_id"""
    def __init__(self):
        self._value = None

    # pylint: disable=arguments-renamed
    def validate(self, orderid):
        """Method for checking the order_id format"""
        try:
            my_order_id_re = re.compile(r"[0-9a-fA-F]{32}$")
            if not my_order_id_re.fullmatch(orderid):
                raise OrderManagementException(ExceptionMessage.ORDER_ID_NOT_VALID.value)
        except KeyError as ex:
            raise OrderManagementException(ExceptionMessage.BAD_LABEL.value) from ex
        return orderid

    @property
    def data(self):
        """method for getting a phone_number"""
        return self._value

    @data.setter
    def data(self, value):
        """method for setting a phone_number"""
        self._value = self.validate(value)
