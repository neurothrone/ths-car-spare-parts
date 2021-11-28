from app.controllers.product import ProductController
from app.controllers.store import StoreController
from app.controllers.supplier import SupplierController
from app.data.models.store import Store, StoreType
from shared.validators import validate_length


# TODO: create a decorator for validating string lengths
# TODO: move validation to controllers


class StoreGenerator:
    STORE_TYPE_MAX_LEN = 1
    PHONE_MAX_LEN = 25
    EMAIL_MAX_LEN = 100

    @staticmethod
    def generate(store_type: str, phone: str, email: str,
                 address: str = None, zip_code: str = None, city: str = None) -> Store:
        validate_length(store_type, StoreGenerator.STORE_TYPE_MAX_LEN)
        validate_length(phone, StoreGenerator.PHONE_MAX_LEN)
        validate_length(email, StoreGenerator.EMAIL_MAX_LEN)

        return StoreController.create(
            store_type=store_type, phone=phone, email=email,
            address=address, zip_code=zip_code, city=city)


def test_store_supplier():
    store = StoreController.find_by_id(1)

    print(store)
    print(store.suppliers)

    supplier = SupplierController.find_by_id(4)
    print(supplier)

    # StoreController.add_supplier_to_store(store, supplier)
    StoreController.remove_supplier_from_store(store, supplier)

    for supplier in store.suppliers:
        print(supplier)

    print(store)


def test_store_fail():
    # store = StoreController.create(store_type=StoreType.PHYSICAL,
    #                                phone="+64 70 722 88 88",
    #                                email="store@example.se")
    store = StoreController.create(store_type=StoreType.ONLINE,
                                   phone="+64 70 722 88 88",
                                   email="store@example.se",
                                   address="Tarbergsgatan 25",
                                   zip_code="172 41",
                                   city="Karlstad")


def test_store_product():
    # TODO: creation
    # store = StoreController.create(store_type=StoreType.PHYSICAL,
    #                                phone="+64 70 722 88 88",
    #                                email="store@example.se",
    #                                address="Tarbergsgatan 25",
    #                                zip_code="172 41",
    #                                city="Karlstad")
    # store = StoreController.create(store_type=StoreType.ONLINE,
    #                                phone="+64 70 722 88 88",
    #                                email="store@example.se")

    # product = ProductController.create(name="Product Name",
    #                                    description="Description",
    #                                    cost=15,
    #                                    price=20)

    # TODO: retrieval
    store = StoreController.find_by_id(1)
    print(store)
    product = ProductController.find_by_id(1)

    # TODO: adding (with defaults and with custom)
    # StoreController.add_product_to_store(store, product)
    # StoreController.add_product_to_store(store,
    #                                      product,
    #                                      stock_number=19,
    #                                      critical_threshold=5,
    #                                      amount_automatic_order=15)

    # TODO: removing
    StoreController.remove_product_from_store(store, product)

    for shp in store.products:
        print(type(shp))
        print(f"\tStock number: {shp.stock_number}")
        print(f"\tCritical threshold: {shp.critical_threshold}")
        print(f"\tAutomatic amount: {shp.amount_automatic_order}")
        print(shp.product)
        print(shp.store)


def main():
    # test_store_fail()
    test_store_product()
    # test_store_supplier()


if __name__ == "__main__":
    main()