import re
from .attribute import Attribute
from .order_management_exception import OrderManagementException


class AddressAttribute(Attribute):
    def __init__(self):
        pass

    def validate(self, address):
        my_address_re = re.compile(r"^(?=^.{20,100}$)(([a-zA-Z0-9]+\s)+[a-zA-Z0-9]+)$")
        if not my_address_re.fullmatch(address):
            raise OrderManagementException("address is not valid")
        return address