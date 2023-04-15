
import re
from .attribute import Attribute
from .order_management_exception import OrderManagementException

class OrderTypeAttribute(Attribute):
    def __init__(self):
        pass
    def validate(self, value):
        my_order_type_re = re.compile(r"(Regular|Premium)")
        if not my_order_type_re.fullmatch(value):
            raise OrderManagementException("order_type is not valid")
        return value