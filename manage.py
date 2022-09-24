

import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder

from app import flask_app
from app.plugins import db
# flake8: noqa
from app.repositories.models import Ingredient, Order, OrderDetail, Size


manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)

seeder = FlaskSeeder()
seeder.init_app(flask_app, db)


@manager.command('test', with_appcontext=False)
def test():
    return pytest.main(['-v', './app/test'])


@manager.command('clear-db', with_appcontext=True)
def clear_db():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table %s' % table)
        db.session.execute(table.delete())
    db.session.commit()


if __name__ == '__main__':
    manager()
