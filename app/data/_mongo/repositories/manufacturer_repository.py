from __future__ import annotations
from typing import Optional


from app.data._mongo.models.product import Product

from app.data._mongo.models.manufacturer import Manufacturer
from app.data._mongo.repositories import BaseRepository


class SupplierRepository(BaseRepository):
    model = Manufacturer



