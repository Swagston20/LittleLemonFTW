from  django.tests import TestCase
from .restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)

#     def test_getall(self):
#         item = Menu.objects.create(title="IceCream", price=80, inventory=100)
#         self.assertEqual(item, "IceCream : 80")