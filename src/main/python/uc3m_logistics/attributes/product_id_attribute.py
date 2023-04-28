"""Module for validating a ean13 code"""
import re
from uc3m_logistics.order_management_exception import OrderManagementException
from uc3m_logistics.attributes.attribute import Attribute
from uc3m_logistics.exception_messages import ExceptionMessage


class ProductIdAttribute(Attribute):
    """Class for validating a ean13 code"""
    def __init__(self):
        self._value = None

    # pylint: disable=arguments-renamed
    def validate(self, ean13):
        """method vor validating a ean13 code"""
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE EAN13
        # RETURN TRUE IF THE EAN13 IS RIGHT, OR FALSE IN OTHER CASE
        checksum = 0
        code_read = -1
        regex_ean13 = re.compile("^[0-9]{13}$")
        valid_ean13_format = regex_ean13.fullmatch(ean13)
        if valid_ean13_format is None:
            raise OrderManagementException(ExceptionMessage.EAN13_NOT_VALID.value)

        for i, digit in enumerate(reversed(ean13)):
            try:
                current_digit = int(digit)
            except ValueError as v_e:
                raise OrderManagementException(ExceptionMessage.EAN13_NOT_VALID.value) from v_e
            if i == 0:
                code_read = current_digit
            else:
                checksum += current_digit * 3 if (i % 2 != 0) else current_digit
        control_digit = (10 - (checksum % 10)) % 10

        if (code_read != -1) and (code_read == control_digit):
            return ean13
        raise OrderManagementException(ExceptionMessage.EAN13_CONTROL_DIGIT_NOT_VALID.value)

    @property
    def data(self):
        """method for getting a phone_number"""
        return self._value

    @data.setter
    def data(self, value):
        """method for setting a phone_number"""
        self._value = self.validate(value)
