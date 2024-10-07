from flask import request, jsonify
from models import db, Departments

def get_departments():
    try:
        data = Departments.query.all()
        return jsonify({'data': data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500
    

def add_departments():
    try:
        data = request.json
        name = data.get('name')
        if not name:
            return jsonify({'message': 'Bad request, name not found'}), 400
        new_data = Departments(name=name)
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'author': {'id': new_data.id, 'name': new_data.name}}), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500
    

def edit_departments(id):
    try:
        data = request.json
        user = Departments.query.get_or_404(id)
        data = request.get_json()
        name = data.get('name', user.name)
        active = data.get('active', user.active)
        if not name and not active:
            return jsonify({'message': 'Bad request, name not found'}), 400
        user.active = active
        user.name = name
        db.session.commit()
        return jsonify({'author': {'id': user.id, 'name': user.name}}), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500