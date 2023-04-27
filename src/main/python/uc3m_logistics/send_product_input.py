"""Send Product class for recieving and validating inputs"""
import json
from uc3m_logistics.attributes.email_attribute import EmailAttribute
from uc3m_logistics.attributes.order_id_attirbute import OrderIdAttribute
from .order_management_exception import OrderManagementException


class SendProductInput():
    """Abstract class for validating attributes"""

    def __init__(self, email, order_id):
        self.__email = EmailAttribute().validate(email)
        self.__order_id = OrderIdAttribute().validate(order_id)

    @property
    def email(self):
        """method for getting a email"""
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = EmailAttribute().validate(email)

    @property
    def order_id(self):
        """method for getting a order_id"""
        return self.__order_id

    @order_id.setter
    def order_id(self, order_id):
        self.__order_id = OrderIdAttribute().validate(order_id)

    @classmethod
    def from_json(cls, file_path):
        """Class method for creating a SendProductInput object from a json file"""
        try:
            with open(file_path, "r", encoding="utf-8", newline="") as json_file:
                data = json.load(json_file)
        except FileNotFoundError as exception:
            raise OrderManagementException("File not found") from exception
        except json.JSONDecodeError as exception:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from exception
        if "OrderID" not in data or "ContactEmail" not in data:
            raise OrderManagementException("Bad label")
        return data
