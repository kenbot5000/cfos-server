from .models import db, Student
from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

student_blueprint = Blueprint('student', __name__)

@student_blueprint.route('/', methods=['GET'])
def get_all_students() :
    students = Student.query.all()
    return jsonify(res = [i.serialize for i in students]), 200

@student_blueprint.route('/', methods=['PUT'])
def add_student() :
    json = request.json
    try :
        student = Student(student_no=json['student_no'], lname=json['lname'], fname=json['fname'])
        db.session.add(student)
        db.session.commit()
        return '', 201
    except IntegrityError :
        return jsonify(res=[{'message' : 'Student already exists'}]), 400

@student_blueprint.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_student_by_id(id) :
    student = Student.query.filter_by(student_no=id).first()
    if(student == None) :
        return '', 404
    if request.method == 'GET' :
        return jsonify(res=student.serialize), 200
    if request.method == 'PUT' :
        student.student_no = request.json['student_no']
        student.fname = request.json['fname']
        student.lname = request.json['lname']
        return jsonify(res = ''), 204
    if request.method == 'DELETE' :
        db.session.delete(student)
        db.session.commit()
        return '', 204