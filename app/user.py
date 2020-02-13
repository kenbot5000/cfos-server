from .models import db, User
from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/', methods=['GET'])
def get_all_users() :
    users = User.query.all()
    return jsonify(res = [i.serialize for i in users]), 200

# TODO Hash password

@users_blueprint.route('/', methods=['PUT'])
def create_user() :
    json = request.json
    try :
        new_user = User(username=json['username'], password=json['password'])
        db.session.add(new_user)
        db.session.commit()
        return '', 201
    except IntegrityError :
        return jsonify(res = [{'message' : 'Username already exists'}]), 400

@users_blueprint.route('/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def search_user_by_id(user_id) :
    user = User.query.filter_by(id=user_id).first()
    if(user == None):
        return '', 404
    if request.method == 'GET' :
        return jsonify(res = user.serialize), 200
    if request.method == 'PUT' :
        user.username = request.json['username']
        user.password = request.json['password']
        db.session.commit()
        return jsonify(res = ''), 204
    if request.method == 'DELETE' :
        db.session.delete(user)
        db.session.commit()
        return '', 204

@users_blueprint.route('/<string:username>', methods=['GET'])
def get_user_by_name(username) :
    user = User.query.filter_by(username=username).first()
    return jsonify(res = user.serialize)
