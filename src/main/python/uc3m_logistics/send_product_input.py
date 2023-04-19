"""Send Product class for recieving and validating inputs"""
import json
from .order_management_exception import OrderManagementException
from uc3m_logistics.attributes.email_attribute import EmailAttribute
from uc3m_logistics.attributes.order_id_attirbute import OrderIdAttribute

class SendProductInput():
    """Abstract class for validating attributes"""
    def __init__(self,email,orderId):
        self.__email = EmailAttribute().validate(email)
        self.__order_id = OrderIdAttribute().validate(orderId)
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
        self.__email = EmailAttribute().validate(email)
    @property
    def order_id(self):
        return self.__order_id

    @order_id.setter
    def order_id(self, orderId):
        self.__order_id = OrderIdAttribute().validate(orderId)
    @classmethod
    def from_json(cls,file_path):
        try:
            with open(file_path,"r",encoding="utf-8",newline="") as json_file:
                data = json.load(json_file)
        except FileNotFoundError as exception:
            raise OrderManagementException("File not found") from exception
        except json.JSONDecodeError as exception:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from exception
        if "OrderID" not in data or "ContactEmail" not in data:
            raise OrderManagementException("Bad label")
        return data

