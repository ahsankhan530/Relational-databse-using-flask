from projet import db, login_manager
from flask_login import UserMixin 
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from projet import app




@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

# class User(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(20))
#     pets=db.relationship('Pet',backref='owner')
# class Pet(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     data=db.Column('data',db.LargeBinary)
#     owner_id=db.Column(db.Integer,db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
     __tablename__ = "user"
     id = db.Column(db.Integer, primary_key=True)
     nom = db.Column(db.String(25), nullable=True)
     prenom = db.Column(db.String(25), nullable=True)
     adresse = db.Column(db.String(100), nullable=True)
     mail = db.Column(db.String(60), unique=True, nullable=True)
     password = db.Column(db.String(60), nullable=True)
     name=db.Column(db.String())
     data=db.Column('data',db.LargeBinary)
     

#      up=db.relationship('Upl',backref='User', lazy='dynamic')
# class Upl(db.Model):
#     __tablename__ = "upl"
#     id=db.Column('upl_id',db.Integer,primary_key=True)
#     data=db.Column('data',db.LargeBinary)
#     owner_id=db.Column(db.Integer,db.ForeignKey('.user.user_id'))
#     user=db.relationship('User')
   

# class Document(db.Model) :
#     id = db.Column(db.Integer, primary_key=True)
#     fichier_url = db.Column(db.String, default=None, nullable=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
   
#     def __repr__(self):
#         return f"Document('{self.id}', '{self.fichier_nom}', '{self.user_id}')"


admin = Admin(app)
admin.add_view(ModelView(User, db.session))