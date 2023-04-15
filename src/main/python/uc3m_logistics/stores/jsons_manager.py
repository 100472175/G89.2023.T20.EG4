"""Module for validating a order_type"""
import json
from uc3m_logistics.order_management_exception import OrderManagementException


class JSON:
    """Class for reading and writing json files"""

    def read_json_register_order(self, file):
        """Method for reading a json file and returning a list of dictionaries"""
        try:
            with open(file, "r", encoding="utf-8", newline="") as file_data:
                data_list = json.load(file_data)
        except FileNotFoundError:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return data_list

    def read_json_send_product(self, file):
        """Method for reading a json file and returning a dictionary"""
        try:
            with open(file, "r", encoding="utf-8", newline="") as file_data:
                data = json.load(file_data)
        except FileNotFoundError as ex:
            # file is not found
            raise OrderManagementException("File is not found") from ex
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return data

    def read_json_deliver_product(self, file):
        """Method for reading a json file and returning a list of dictionaries"""
        try:
            with open(file, "r", encoding="utf-8", newline="") as file_data:
                data_list = json.load(file_data)
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        except FileNotFoundError as ex:
            raise OrderManagementException("shipments_store not found") from ex
        return data_list

    def write_json(self, file, content):
        """Method for writing a json file"""
        try:
            with open(file, "w", encoding="utf-8", newline="") as file_data:
                json.dump(content, file_data, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex
        return True
