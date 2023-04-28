"""FILE FOR STORING THE ERROR MESSAGES"""
from enum import Enum


class ExceptionMessage(Enum):
    """Class to store the messages of the exceptions"""
    JSON_DECODE_ERROR = "JSON Decode Error - Wrong JSON Format"
    WRONG_FILE_OR_PATH = "Wrong file or file path"
    FILE_NOT_FOUND = "File not found"

    # Order requests
    ORDER_ID_NOT_FOUND = "order_id not found"
    ORDER_ID_ALREADY_REGISTERED = "order_id is already registered in orders_store"
    BAD_LABEL = "Bad label"
    # Order shipping
    TRACKING_CODE_NOT_FOUND = "tracking_code is not found"
    DATE_NOT_VALID = "Today is not the delivery date"
    # Manipulated data
    ORDERS_DATA_MANIPULATED = "Orders' data have been manipulated"

    # Attributes
    ADDRESS_NOT_VALID = "address is not valid"
    EAN13_NOT_VALID = "Invalid EAN13 code string"
    EAN13_CONTROL_DIGIT_NOT_VALID = "Invalid EAN13 control digit"
    EMAIL_NOT_VALID = "contact email is not valid"
    ORDER_ID_NOT_VALID = "order id is not valid"
    ORDER_TYPE_NOT_VALID = "order_type is not valid"
    PHONE_NUMBER_NOT_VALID = "phone number is not valid"
    TRACKING_CODE_NOT_VALID = "tracking_code format is not valid"
    ZIP_CODE_NOT_VALID = "zip_code is not valid"
    ZIP_CODE_FORMAT_NOT_VALID = "zip_code format is not valid"
