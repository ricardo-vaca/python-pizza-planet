from app.plugins import db


class OrderDetail(db.Model):
    _id = db.Column(
        db.Integer,
        primary_key=True
    )

    order_id = db.Column(
        db.Integer,
        db.ForeignKey('order._id')
    )

    ingredient = db.relationship(
        'Ingredient',
        backref=db.backref('ingredient')
    )
    ingredient_id = db.Column(
        db.Integer,
        db.ForeignKey('ingredient._id')
    )
    ingredient_price = db.Column(db.Float)

    beverage = db.relationship(
        'Beverage',
        backref=db.backref('beverage')
    )
    beverage_id = db.Column(
        db.Integer,
        db.ForeignKey('beverage._id')
    )
    beverage_price = db.Column(db.Float)
