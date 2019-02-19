import unittest

from grocery_list_classes import *

class ShoppingListTests(unittest.TestCase):

    def setUp(self):
        self.shoppinglist = ShoppingList()
        print("SETUP")

    def test_list_total(self):
        print("test_list_total")
        result = self.shoppinglist.list_total(2, 4)
        self.assertEqual(8, result)

    def tearDown(self):
        print("TEARDOWN")

    unittest.main()
