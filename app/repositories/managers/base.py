from typing import Optional, Any


from app.common.base_factory import BaseFactory
from ...plugins import db, ma


class BaseManager(BaseFactory):

    def __init__(
        self,
        model: Optional[db.Model] = None,
        serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    ):
        self.model = model
        self.serializer = serializer
        self.session = db.session

    def get_all(self):
        serializer = self.serializer(many=True)
        _objects = self.model.query.all()
        result = serializer.dump(_objects)
        return result

    def get_by_id(self, _id: Any):
        entry = self.model.query.get(_id)
        return self.serializer().dump(entry)

    def create(self, entry: dict):
        serializer = self.serializer()
        new_entry = serializer.load(entry)
        self.session.add(new_entry)
        self.session.commit()
        return serializer.dump(new_entry)

    def update(self, _id: Any, new_values: dict):
        self.session.query(self.model).filter_by(_id=_id).update(new_values)
        self.session.commit()
        return self.get_by_id(_id)
