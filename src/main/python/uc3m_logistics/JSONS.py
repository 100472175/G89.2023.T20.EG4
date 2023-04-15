import json
from .order_management_exception import OrderManagementException

class JSON:
    def __init__(self):
        pass
    def read_json_register_order(self,file):
        try:
            with open(file, "r", encoding="utf-8", newline="") as f:
                data_list = json.load(f)
        except FileNotFoundError:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return data_list

    def read_json_send_product(self, file):
        try:
            with open(file, "r", encoding="utf-8", newline="") as f:
                data = json.load(f)
        except FileNotFoundError as ex:
            # file is not found
            raise OrderManagementException("File is not found") from ex
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return data

    def write_json(self,file,content):
        try:
            with open(file, "w", encoding="utf-8", newline="") as f:
                json.dump(content, f, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex
        return True
