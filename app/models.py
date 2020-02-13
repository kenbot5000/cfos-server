from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model) :
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    @property
    def serialize(self) :
        return {
            'id' : self.id,
            'username' : self.username,
            'password' : self.password
        }

class Menu(db.Model) :
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    # Add food type perhaps? To allow sorting by food/drink/etc

    @property
    def serialize(self) :
        return {
            'id' : self.id,
            'name' : self.name,
            'price' : self.price,
            'active' : self.active
        }


# @property
# def serialize_many2many(self):
#     """
#        Return object's relations in easily serializable format.
#        NB! Calls many2many's serialize property.
#        """
#     return [item.serialize for item in self.many2many]
