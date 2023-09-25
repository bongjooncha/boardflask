import pymysql
from flask import Flask
from api import board
from db_connect import db
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.register_blueprint(board)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:12345678@localhost:3306/a"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] ="Secret key"

db.init_app(app)
bcrypt = Bcrypt(app)

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)