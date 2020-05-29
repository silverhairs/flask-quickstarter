from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

pages_dir = os.path.abspath('project/pages/')
app = Flask(__name__, template_folder=pages_dir)
app.config['SECRET_KEY'] = 'f5e50b1a6d6774d3d4f9206eba430a4d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from project import routes