import re
from .attribute import Attribute
from uc3m_logistics.order_management_exception import OrderManagementException


class ProductIdAttribute(Attribute):
    def __init__(self):
        pass

    def validate(self, ean13):
        """method vor validating a ean13 code"""
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE EAN13
        # RETURN TRUE IF THE EAN13 IS RIGHT, OR FALSE IN OTHER CASE
        checksum = 0
        code_read = -1
        regex_ean13 = re.compile("^[0-9]{13}$")
        valid_ean13_format = regex_ean13.fullmatch(ean13)
        if valid_ean13_format is None:
            raise OrderManagementException("Invalid EAN13 code string")

        for i, digit in enumerate(reversed(ean13)):
            try:
                current_digit = int(digit)
            except ValueError as v_e:
                raise OrderManagementException("Invalid EAN13 code string") from v_e
            if i == 0:
                code_read = current_digit
            else:
                checksum += (current_digit) * 3 if (i % 2 != 0) else current_digit
        control_digit = (10 - (checksum % 10)) % 10

        if (code_read != -1) and (code_read == control_digit):
            return ean13
        raise OrderManagementException("Invalid EAN13 control digit")