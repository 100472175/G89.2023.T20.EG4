"""Contains the class OrderDelivery"""
from uc3m_logistics.attributes.tracking_code_attribute import TrackingCodeAttribute
from uc3m_logistics.stores.order_delivery_store import OrderDeliveryStore
from uc3m_logistics.stores.order_shipping_store import OrderShippingStore


# pylint: disable=too-many-instance-attributes
class OrderDelivery():
    """Class representing the shipping of an order"""

    def __init__(self, tracking_code):
        self.__tracking_code = TrackingCodeAttribute().validate(tracking_code)

    @property
    def tracking_code(self):
        """Returns the tracking code"""
        return self.__tracking_code

    @tracking_code.setter
    def tracking_code(self, value):
        self.__tracking_code = TrackingCodeAttribute().validate(value)

    def save_to_store(self):
        """Saves the order to the store"""
        my_order = OrderShippingStore()
        my_order.find_item_by_key(self.__tracking_code)
        my_order_delivery = OrderDeliveryStore()
        my_order_delivery.add_item(self.__tracking_code)
        return True
