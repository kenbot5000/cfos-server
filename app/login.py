from .models import db, User
from flask import Blueprint, jsonify, request, session, current_app
from sqlalchemy.exc import IntegrityError

import jwt
import datetime
from functools import wraps

login_blueprint = Blueprint('login', __name__)

def token_required(f) :
    @wraps(f)
    def decorated(*args, **kwargs) :
        print('THIS FIRES')
        token = session.get('token')

        if not token :
            return jsonify(res = [{'message' : 'Login required'}]), 401
        
        try :
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except :
            return jsonify(res = [{'message' : 'Token is invalid'}])

        return f(*args, **kwargs)

@login_blueprint.route('/', methods=['POST'])
def login() :
    creds = request.json
    try : 
        usercheck = User.query.filter_by(username=creds['username']).first()
        if creds['password'] == usercheck.password :
            token = jwt.encode({'user' : creds['username'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours=8)}, current_app.config['SECRET_KEY'])
            session['token'] = token
            return jsonify({'token' : token.decode('UTF-8')})
    except IntegrityError :
        return jsonify(res = [{'message' : 'User does not exist'}])