from .models import db, Menu
from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

menu_blueprint = Blueprint('menu', __name__)

@menu_blueprint.route('/', methods=['GET'])
def get_all_menu_items() :
    menu = Menu.query.all()
    return jsonify(res = [i.serialize for i in menu]), 200

@menu_blueprint.route('/', methods=['PUT'])
def create_menu_item() :
    json = request.json
    try :
        # if(json['name'] is int) :
            # return jsonify(res=[{'message' : 'Name must be alphanumeric, but not numbers only.'}]), 400
        menu_item = Menu(name=json['name'], price=json['price'], active=json['active'])
        db.session.add(menu_item)
        db.session.commit()
        return '', 201
    except IntegrityError :
        return jsonify(res=[{'message': 'Item already exists'}]), 400

@menu_blueprint.route('/<int:menu_id>', methods=['GET', 'PUT', 'DELETE'])
def search_menu_by_id(menu_id) :
    menu_item = Menu.query.filter_by(id=menu_id).first()
    if(menu_item == None):
        return '', 404
    if request.method == 'GET' :
        return jsonify(res=menu_item.serialize), 200
    if request.method == 'PUT' :
        menu_item.name = request.json['name']
        menu_item.price = request.json['price']
        menu_item.active = request.json['active']
    if request.method == 'DELETE' :
        db.session.delete(menu_item)
        db.session.commit()

@menu_blueprint.route('/<string:menu_name>', methods=['GET'])
def search_menu_by_name(menu_name) :
    menu_item = Menu.query.filter_by(name=menu_name).first()
    if(menu_item == None):
        return '', 404
    else :
        return jsonify(res=menu_item.serialize), 200
