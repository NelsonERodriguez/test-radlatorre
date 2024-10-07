from flask import Flask
from controllers.departments import get_departments, add_departments

app = Flask(__name__)
port = 5000

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:123456@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/authors', methods=['GET'])
def g_departments():
    return get_departments()


@app.route('/authors', methods=['GET'])
def a_departments():
    return add_departments()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=port)
