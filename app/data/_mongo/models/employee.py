from app.data._mongo.db import db
from app.data._mongo.models import BaseDocument


class Employee(BaseDocument["Employee"]):
    collection = db.employees
