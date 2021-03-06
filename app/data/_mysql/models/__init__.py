from __future__ import annotations
from abc import abstractmethod
from typing import Generic, TypeVar, Optional

from app.data._mysql.db import Base

TBaseModel = TypeVar("TBaseModel", bound="BaseModel")


class BaseModel(Generic[TBaseModel], Base):
    __abstract__ = True

    def __repr__(self) -> str:
        attributes = ", ".join(f"{k}={v}" for k, v in self.to_dict().items())
        return f"{self.__class__.__name__}({attributes})"

    def __str__(self) -> str:
        attributes = "\n".join(f"\t{k}: {v}" for k, v in self.to_dict().items())
        return f"{self.__class__.__name__}:\n{attributes}"

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if k != "_sa_instance_state"}

    @abstractmethod
    def id(self) -> Optional[int | str]:
        pass


from app.data._mysql.models.car import Car
from app.data._mysql.models.car_detail import CarDetail
from app.data._mysql.models.contact_person import ContactPerson
from app.data._mysql.models.customer import Customer
from app.data._mysql.models.employee import Employee
from app.data._mysql.models.manufacturer import Manufacturer
from app.data._mysql.models.order import Order
from app.data._mysql.models.order_detail import OrderDetail
from app.data._mysql.models.product import Product
from app.data._mysql.models.storage import Storage
from app.data._mysql.models.store import Store
from app.data._mysql.models.supplier import Supplier

from app.data._mysql.models.associations.car_details_has_products import car_details_has_products
from app.data._mysql.models.associations.products_has_manufacturers import products_has_manufacturers
from app.data._mysql.models.associations.products_has_suppliers import products_has_suppliers
from app.data._mysql.models.associations.stores_has_suppliers import stores_has_suppliers
