# Initialize the web interface package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SECRET_KEY"] = "nova_genesis_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nova_genesis.db"
db = SQLAlchemy(app)
login_manager = LoginManager(app)
bootstrap = Bootstrap(app)

from .app import routes
