import unittest

from app.settings import Settings

Settings.TESTING = True

from app.controllers.manufacturer_controller import ManufacturerController
from app.controllers.product_controller import ProductController
from generators.product_generator import ProductGenerator
from generators.contact_person_generator import ContactPersonGenerator
from generators.manufacturer_generator import ManufacturerGenerator
from shared.tests.test_printer import TestPrinter


class ManufacturerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        ContactPersonGenerator.populate_database(amount=100)
        ManufacturerGenerator.populate_database(amount=1)
        ProductGenerator.populate_database(amount=2)
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        TestPrinter.print_passed_tests()

    def test_add_product_to_manufacturer(self):
        product = ProductController.find_all()[0]
        product_two = ProductController.find_all()[1]
        manufacturer = ManufacturerController.find_all()[0]
        ManufacturerController.add_product_to_manufacturer(manufacturer, product)
        ManufacturerController.add_product_to_manufacturer(manufacturer, product_two)
        print('----- The two products are: -----')
        for manufacturers_product in manufacturer.products:
            print(manufacturers_product.name)
            self.assertIsNotNone(manufacturers_product)
        TestPrinter.add(self.test_add_product_to_manufacturer.__name__)

    def test_remove_product_from_manufacturer(self):
        product = ProductController.find_all()[0]
        product_two = ProductController.find_all()[1]
        manufacturer = ManufacturerController.find_all()[0]

        ManufacturerController.add_product_to_manufacturer(manufacturer, product)
        ManufacturerController.add_product_to_manufacturer(manufacturer, product_two)

        ManufacturerController.remove_product_from_manufacturer(manufacturer, product)
        ManufacturerController.remove_product_from_manufacturer(manufacturer, product_two)

        for manufacturers_product in manufacturer.products:
            self.assertIsNone(manufacturers_product.name)
        TestPrinter.add(self.test_remove_product_from_manufacturer.__name__)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
