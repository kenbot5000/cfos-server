from .models import db, Order, OrderItem, Menu, Student
from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from pprint import pprint

order_blueprint = Blueprint('order', __name__)

# JSON Format
# {
# "student_no" : 2000028158,
# "orders" : [1, 2, 3, 4]
# }

# TODO add reference number

@order_blueprint.route('/', methods=['PUT'])
def make_order() :
    req = request.json
    try :
        student = Student.query.filter_by(student_no = req['student_no']).first()
        order = Order(student_no=student.serialize['student_no'])
        db.session.add(order)
        db.session.commit()
        for item in request.json['orders'] :
            new_item = OrderItem(order_id=order.serialize['order_no'], menu_id=item)
            db.session.add(new_item)
        db.session.commit()
        return '', 201
    except IntegrityError as ex :
        pprint(ex)
        return '', 204

@order_blueprint.route('/', methods=['GET'])
def get_all_orders() :
    orders = Order.query.all()
    return jsonify(res = [i.serialize for i in orders]), 200

@order_blueprint.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_order(id) :
    order = Order.query.filter_by(order_no=id).first()
    if request.method == 'DELETE' :
        db.session.delete(order)
        db.session.commit()
        return '', 204
    if request.method == 'PUT' :
        req = request.json
        new_item = OrderItem(order_id=id, menu_id=request.json['order'])
        db.session.add(new_item)
        db.session.commit()
        return '', 201

@order_blueprint.route('/<int:id>/items', methods=['GET'])
def get_items_under_order(id) :
    items = OrderItem.query.filter_by(order_id=id).all()
    res = {}
    res['order_id'] = items[0].order_id
    print(items)
    res['orders'] = [i.serialize['menu_id'] for i in items]
    return jsonify(res), 200
