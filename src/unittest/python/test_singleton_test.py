"""Test for singleton for Order Manager"""
from unittest import TestCase
from uc3m_logistics import OrderManager
from uc3m_logistics.stores.order_request_store import OrderRequestStore
from uc3m_logistics.stores.order_shipping_store import OrderShippingStore
from uc3m_logistics.stores.order_delivery_store import OrderDeliveryStore

class TestSingleton(TestCase):
    """Class for testing singleton"""
    def test_singleton_order_manager(self):
        """singleton test for order manager"""
        om1 = OrderManager()
        om2 = OrderManager()

        self.assertEqual(id(om1),id(om2))
    def test_singleton_order_request_store(self):
        """singleton test for order manager"""
        om1 = OrderRequestStore()
        om2 = OrderRequestStore()
"""
        self.assertEqual(id(om1),id(om2))
    def test_singleton_order_shipping_store(self):
        
        om1 = OrderShippingStore()
        om2 = OrderShippingStore()

        self.assertEqual(id(om1),id(om2))
    def test_singleton_order_delivery_store(self):
        om1 = OrderDeliveryStore()
        om2 = OrderDeliveryStore()

        self.assertEqual(id(om1),id(om2))
"""
