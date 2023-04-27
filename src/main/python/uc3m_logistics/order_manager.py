"""Module that control everything, the manager"""
from uc3m_logistics.order_request import OrderRequest
from uc3m_logistics.order_shipping import OrderShipping
from uc3m_logistics.order_delivery import OrderDelivery


# NEW IMPORTS FOR STORES

class OrderManager:
    """Class for providing the methods for managing the orders process"""

    class __OrderManager():
        def __init__(self):
            pass

        # pylint: disable=too-many-arguments
        def register_order(self, product_id,
                           order_type,
                           address,
                           phone_number,
                           zip_code):
            """Register the orders into the order's file"""

            my_order = OrderRequest(product_id=product_id,
                                    order_type=order_type,
                                    delivery_address=address,
                                    phone_number=phone_number,
                                    zip_code=zip_code)
            my_order.save_to_store()

            return my_order.order_id

        # pylint: disable=too-many-locals
        def send_product(self, input_file):
            """Sends the order included in the input_file"""
            order_shipping = OrderShipping.from_send_input_file(input_file)

            order_shipping.save_to_store()
            return order_shipping.tracking_code

        def deliver_product(self, tracking_code):
            """Register the delivery of the product"""
            my_order_delivery = OrderDelivery(tracking_code)
            return my_order_delivery.save_to_store()

    instance = None

    def __new__(cls):
        if not OrderManager.instance:
            OrderManager.instance = OrderManager.__OrderManager()
        return OrderManager.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)

    def __init__(self):
        pass
