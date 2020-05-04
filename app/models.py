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

class Student(db.Model) :
    __tablename__ = 'student'
    student_no = db.Column(db.Integer, primary_key=True, autoincrement=False)
    lname = db.Column(db.String(50), nullable=False)
    fname = db.Column(db.String(50), nullable=False)
    orders = db.relationship('Order')
    
    @property
    def serialize(self) :
        return {
            'student_no' : self.student_no,
            'lname' : self.lname,
            'fname' : self.fname
        }

class Order(db.Model) :
    __tablename__ = 'order'
    order_no = db.Column(db.Integer, primary_key=True)
    student_no = db.Column(db.Integer, db.ForeignKey('student.student_no'))
    order_items = db.relationship('OrderItem')

    @property
    def serialize(self) :
        return {
            'order_no' : self.order_no,
            'student_no' : self.student_no,
        }

class OrderItem(db.Model) :
    __tablename__ = 'orderitem'
    order_item_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_no'))
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))
    menu = db.relationship('Menu')

    @property
    def serialize(self) :
        return {
            'order_id' : self.order_id,
            'order_item_no' : self.order_item_no,
            'menu_id' : self.menu_id
        }

# @property
# def serialize_many2many(self):
#     """
#        Return object's relations in easily serializable format.
#        NB! Calls many2many's serialize property.
#        """
#     return [item.serialize for item in self.many2many]
