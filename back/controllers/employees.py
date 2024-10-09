from flask import Blueprint, jsonify, request
from models import db, Employees

employees_bp = Blueprint('employees', __name__)

@employees_bp.route('/', methods=['POST'])
def crear_empleado():
    data = request.json
    nuevo_empleado = Employees(
        nombre=data['nombre'],
        puesto_id=data['puesto_id'],
        departamento_id=data['departamento_id']
    )
    db.session.add(nuevo_empleado)
    db.session.commit()
    return jsonify(nuevo_empleado.to_dict()), 201

@employees_bp.route('/', methods=['GET'])
def obtener_empleados():
    empleados = Employees.query.all()
    return jsonify([empleado.to_dict() for empleado in empleados]), 200

@employees_bp.route('/<int:id>', methods=['GET'])
def obtener_empleado(id):
    empleado = Employees.query.get_or_404(id)
    return jsonify(empleado.to_dict()), 200

@employees_bp.route('/<int:id>', methods=['PUT'])
def actualizar_empleado(id):
    empleado = Employees.query.get_or_404(id)
    data = request.json
    empleado.nombre = data.get('nombre', empleado.nombre)
    empleado.puesto_id = data.get('puesto_id', empleado.puesto_id)
    empleado.departamento_id = data.get('departamento_id', empleado.departamento_id)
    db.session.commit()
    return jsonify(empleado.to_dict()), 200
