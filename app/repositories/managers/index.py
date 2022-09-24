from sqlalchemy.sql import text, column

from ..managers import BaseManager


class IndexManager(BaseManager):

    def __init__(self, model=None, serializer=None):
        super().__init__(model, serializer)

    def test_connection(self):
        self.session.query(column('1')).from_statement(
            text('SELECT 1')
        ).all()
