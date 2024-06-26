"""MODULE: order_request. Contains the order request class"""
import hashlib
import json
from datetime import datetime
# Imports for validating parameters
from uc3m_logistics.attributes.order_type_attribute import OrderTypeAttribute
from uc3m_logistics.attributes.zip_code_attribute import ZipCodeAttribute
from uc3m_logistics.attributes.phone_number_attribute import PhoneNumberAttribute
from uc3m_logistics.attributes.product_id_attribute import ProductIdAttribute
from uc3m_logistics.attributes.address_attribute import AddressAttribute


class OrderRequest:
    """Class representing the register of the order in the system"""

    # pylint: disable=too-many-arguments
    def __init__(self, product_id, order_type,
                 delivery_address, phone_number, zip_code):
        self.__product_id = ProductIdAttribute().validate(product_id)
        self.__delivery_address = AddressAttribute().validate(delivery_address)
        self.__order_type = OrderTypeAttribute().validate(order_type)
        self.__phone_number = PhoneNumberAttribute().validate(phone_number)
        self.__zip_code = ZipCodeAttribute().validate(zip_code)
        justnow = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(justnow)
        self.__order_id = hashlib.md5(self.__str__().encode()).hexdigest()

    def __str__(self):
        return "OrderRequest:" + json.dumps(self.__dict__)


    def save_to_store(self):
        """Saves the order request to the store"""
        # Import for only this part of the code
        from uc3m_logistics.stores.order_request_store import OrderRequestStore
        OrderRequestStore().add_item(self)

    @property
    def delivery_address(self):
        """Property representing the address where the product
        must be delivered"""
        return self.__delivery_address

    @delivery_address.setter
    def delivery_address(self, value):
        self.__delivery_address = AddressAttribute().validate(value)

    @property
    def order_type(self):
        """Property representing the type of order: REGULAR or PREMIUM"""
        return self.__order_type

    @order_type.setter
    def order_type(self, value):
        self.__order_type = OrderTypeAttribute().validate(value)

    @property
    def phone_number(self):
        """Property representing the clients's phone number"""
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = PhoneNumberAttribute().validate(value)

    @property
    def product_id(self):
        """Property representing the products  EAN13 code"""
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = ProductIdAttribute().validate(value)

    @property
    def time_stamp(self):
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def order_id(self):
        """Returns the md5 signature"""
        return self.__order_id

    @property
    def zip_code(self):
        """Returns the order's zip_code"""
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, value):
        self.__zip_code = ZipCodeAttribute().validate(value)
