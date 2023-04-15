from .attribute import Attribute
from .order_management_exception import OrderManagementException

class ZipCodeAttribute(Attribute):
    def __init__(self):
        pass
    def validate(self, zip_code):
        if zip_code.isnumeric() and len(zip_code) == 5:
            if (int(zip_code) > 52999 or int(zip_code) < 1000):
                raise OrderManagementException("zip_code is not valid")
        else:
            raise OrderManagementException("zip_code format is not valid")
        return zip_code