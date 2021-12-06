from typing import Optional
from app.data._mysql.db import session
from app.data._mysql.models import ContactPerson
from app.data._mysql.models.supplier import Supplier
from app.data._mysql.models.product import Product
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.repositories.contact_person_repository import ContactPersonRepository


class SupplierRepository(BaseRepository):
    model = Supplier

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Supplier]:
        return session.query(cls.model).filter_by(supplier_id=_id).first()

    @classmethod
    def add_contact_person(cls, supplier: Supplier, contact_person: ContactPerson) -> None:
        if cls.has_contact_person(supplier):
            return

        supplier.contact_person_id = contact_person.contact_person_id
        contact_person.supplier = supplier
        session.commit()

    @classmethod
    def remove_contact_person(cls, supplier: Supplier) -> None:
        if not cls.has_contact_person(supplier):
            return

        contact_person = ContactPersonRepository.find_by_id(supplier.contact_person_id)
        contact_person.supplier = None
        supplier.contact_person_id = None
        session.commit()

    @staticmethod
    def add_product_to_supplier(supplier: Supplier,
                                product: Product) -> None:
        if SupplierRepository.has_product(supplier, product):
            return

        supplier.products.append(product)
        session.commit()

    @staticmethod
    def remove_product_from_supplier(supplier: Supplier,
                                     product: Product) -> None:
        if SupplierRepository.has_product(supplier, product):
            return

        supplier.products.remove(product)
        session.commit()

    @classmethod
    def has_contact_person(cls, supplier: Supplier) -> bool:
        return supplier.contact_person_id is not None

    @staticmethod
    def has_product(supplier: Supplier, product: Product) -> bool:
        for shp in supplier.products:
            if shp.product.product_id == product.product_id:
                return True
        return False
