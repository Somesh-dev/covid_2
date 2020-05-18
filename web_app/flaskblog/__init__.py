from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail




app = Flask(__name__) 
# app = Flask(__name__, static_url_path='/templates')
app.config['SECRET_KEY'] = '8c5963ea5bf3d00e8e44e3a366639d15'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'hello_login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'samirkhusi108@gmail.com'
app.config['MAIL_PASSWORD'] = '<password>'
mail = Mail(app)


from flaskblog import routes


