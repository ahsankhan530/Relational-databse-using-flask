from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# from flask_uploads import UploadSet, configure_uploads

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'pdf', 'doc', 'docx'])
app.config['SECRET_KEY'] = 'lamine'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

	# fichier = UploadSet('fichier')
	# configure_uploads(app, fichier)

from projet import routes
