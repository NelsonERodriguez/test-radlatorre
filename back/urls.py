from flask import Flask
from controllers.employees import employees_bp
from controllers.departments import departments_bp
from controllers.roles import roles_bp

app = Flask(__name__)

app.register_blueprint(roles_bp, url_prefix='/roles')
app.register_blueprint(departments_bp, url_prefix='/departments')
app.register_blueprint(employees_bp, url_prefix='/employees')

if __name__ == '__main__':
    app.run(debug=True)