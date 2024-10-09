from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Roles, Departments, Employees
# from controllers.departments import get_departments, add_departments

app = Flask(__name__)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gruposis:password@localhost/radlatorre'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

with app.app_context():
    db.create_all()


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True, port=port)
