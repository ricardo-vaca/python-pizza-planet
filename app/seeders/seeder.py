from flask_seeder import Seeder, Faker, generator
from random import randint
from datetime import datetime

from app.repositories.models import Beverage, Ingredient, \
    Order, OrderDetail, Size
from app.seeders.fake_data import fake_beverages, \
    fake_clients, fake_ingredients, fake_sizes


class DataSeeder(Seeder):

    def create_items(self, model, fake_data: tuple):
        faker = Faker(
            cls=model,
            init={
                '_id': generator.Sequence(end=len(fake_data)),
                'name': '',
                'price': 0,
            }
        )

        store = faker.create(len(fake_data))
        for data in store:
            data.name = fake_data[data._id - 1]['name']
            data.price = fake_data[data._id - 1]['price']

        return store

    def create_orders(self):
        customers = fake_clients()
        sizes = fake_sizes()

        faker = Faker(
            cls=Order,
            init={
                'client_name': '',
                'client_dni': '',
                'client_address': '',
                'client_phone': '',
                'date': None,
                'total_price': 0,
                'size_id': generator.Integer(end=len(fake_sizes())),
            }
        )

        store = faker.create(100)
        for order in store:
            customer = customers[randint(0, 4)]
            size = sizes[order.size_id - 1]

            order.total_price = size['price']
            order.client_name = customer['client_name']
            order.client_dni = customer['client_dni']
            order.client_address = customer['client_address']
            order.client_phone = customer['client_phone']
            order.date = datetime(year=2022, month=randint(1, 12), day=1)

        return store

    def create_order_details(self, orders):
        ingredients = fake_ingredients()
        beverages = fake_beverages()

        faker = Faker(
            cls=OrderDetail,
            init={
                'order_id': generator.Integer(end=100),
                'ingredient_price': 0,
                'beverage_price': 0
            }
        )

        store = faker.create(100 * 6)
        for order_detail in store:
            if randint(0, 1) == 1:
                rand_id = randint(0, 9)
                order_detail.ingredient_id = \
                    rand_id + 1
                order_detail.ingredient_price = \
                    ingredients[rand_id]['price']
                orders[order_detail.order_id -
                       1].total_price += order_detail.ingredient_price

            else:
                rand_id = randint(0, 4)
                order_detail.beverage_id = \
                    rand_id + 1
                order_detail.beverage_price = \
                    beverages[rand_id]['price']
                orders[order_detail.order_id -
                       1].total_price += order_detail.beverage_price

        return store

    def run(self):
        self.db.session.add_all(
            self.create_items(Size, fake_sizes())
        )
        self.db.session.add_all(
            self.create_items(Ingredient, fake_ingredients())
        )
        self.db.session.add_all(
            self.create_items(Beverage, fake_beverages())
        )

        orders = self.create_orders()
        self.db.session.add_all(orders)
        self.db.session.add_all(self.create_order_details(orders))

        self.db.session.commit()
