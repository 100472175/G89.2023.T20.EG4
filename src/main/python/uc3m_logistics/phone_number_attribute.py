import re
from .attribute import Attribute
from .order_management_exception import OrderManagementException

class PhoneNumberAttribute(Attribute):
    def __init__(self):
        pass
    def validate(self, phone_number):
        my_phone_number_re = re.compile(r"^(\+)[0-9]{11}")
        if not my_phone_number_re.fullmatch(phone_number):
            raise OrderManagementException("phone number is not valid")
        return phone_number