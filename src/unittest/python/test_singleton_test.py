from unittest import TestCase
from uc3m_logistics import OrderManager
class TestSingleton(TestCase):
    def test_singleton_order_manager(self):
        om1 = OrderManager()
        om2 = OrderManager()
        om3 = OrderManager()

        self.assertEqual(om1,om2)
        self.assertEqual(om1, om3)
        self.assertEqual(om2, om3)
