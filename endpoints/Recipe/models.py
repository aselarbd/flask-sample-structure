from shared.utils import get_db_ref


db = get_db_ref()


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    ingredient = db.Column(db.String(100))
    unit = db.Column(db.String(10))
    qty = db.Column(db.Integer)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
