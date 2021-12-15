from app.controllers.customer_controller import CustomerController
from app.controllers.employee_controller import EmployeeController
from app.controllers.product_controller import ProductController
from app.controllers.storage_controller import StorageController
from app.controllers.store_controller import StoreController
from generators.customer_generator import CustomerGenerator
from generators.employee_generator import EmployeeGenerator
from generators.product_generator import ProductGenerator
from generators.storage_generator import StorageGenerator
from generators.store_generator import StoreGenerator


def populate_db():
    StoreGenerator.populate_database(amount=10)
    EmployeeGenerator.populate_database(amount=30)
    EmployeeController.connect_employees_to_stores(min_=1, max_=3)
    CustomerGenerator.populate_database(amount=30)
    ProductGenerator.populate_database(amount=50)
    StorageGenerator.add_products_to_stores(min_per_store=1, max_per_store=5)


def delete_data_from_mysql_db():
    StorageController.delete_all()
    CustomerController.delete_all()
    EmployeeController.delete_all()
    ProductController.delete_all()
    StoreController.delete_all()


def main():
    # populate_db()
    delete_data_from_mysql_db()
    # EmployeeController.connect_employees_to_stores(min_=1, max_=3)
    # EmployeeController.reset_all_employees_store()

    # StoreGenerator.populate_database(amount=100)
    # StoreGenerator.add_products_to_stores(min_per_store=1, max_per_store=5)
    # StoreGenerator.print_products_in_stores()
    # StoreGenerator.remove_all_products_in_stores()


if __name__ == "__main__":
    main()
