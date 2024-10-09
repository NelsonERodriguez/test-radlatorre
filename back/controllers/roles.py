from flask import Blueprint, jsonify, request
from models import db, Roles
roles_bp = Blueprint('roles', __name__)

@roles_bp.route('/', methods=['POST'])
def add_roles():
    try:
        data = request.json
        name = data.get('name')
        if not name:
            return jsonify({'message': 'Bad request, name not found'}), 400
        new_data = Roles(name=name)
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'data': {'id': new_data.id, 'name': new_data.name}}), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500


@roles_bp.route('/', methods=['GET'])
def get_roles():
    try:
        data = Roles.query.all()
        return jsonify({'data': data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500
    

@roles_bp.route('/<int:id>', methods=['GET'])
def get_role():
    try:
        data = Roles.query.get_or_404(id)
        return jsonify({'data': data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500
    

    
@roles_bp.route('/<int:id>', methods=['PUT'])
def edit_roles(id):
    try:
        data = request.json
        user = Roles.query.get_or_404(id)
        data = request.json
        name = data.get('name', user.name)
        active = data.get('active', user.active)
        if not name and not active:
            return jsonify({'message': 'Bad request, name not found'}), 400
        user.active = active
        user.name = name
        db.session.commit()
        return jsonify({'data': {'id': user.id, 'name': user.name}}), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500