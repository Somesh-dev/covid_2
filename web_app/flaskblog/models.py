
from flaskblog import db, login_manager, app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	
	
	
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	phone = db.Column(db.Integer,unique=True, nullable=False)

	firstname = db.Column(db.String(20), unique=False, nullable=False)
	lastname = db.Column(db.String(20), unique=False, nullable=False)
	pincode = db.Column(db.Integer, unique=False, nullable=False)
	pin_state = db.Column(db.String(20), unique=False, nullable=False)

	image_file = db.Column(db.String(20), nullable=False, default='default.png')
	password = db.Column(db.String(60), nullable=False)

	contaminated = db.Column(db.String(14), nullable=False, default='contaminated')
	times = db.Column(db.Integer, nullable=False, default=1)
	state = db.Column(db.Integer, nullable=False, default=0)
	prev = db.Column(db.Integer, nullable=False, default=0)

	s1 = db.Column(db.Integer, nullable=False, default=0)
	d1 = db.Column(db.Integer, nullable=False, default=0)

	near = db.Column(db.Integer, nullable=False, default=0)

	med_name = db.Column(db.String, nullable=False, default= 'No Shop')
	med_pin = db.Column(db.Integer, unique=False, nullable=True)
	med_verify = db.Column(db.Integer, unique=False, nullable=False, default='not')
	med_link = db.Column(db.String, nullable=True)
	med_avail = db.Column(db.String, nullable=False, default='Details not provided')
	med_edit = db.Column(db.Integer, unique=False,nullable=False, default=0)

	def get_reset_token(self, expires_sec=1000):
		s = Serializer(app.config['SECRET_KEY'], expires_sec)
		return s.dumps({'user_id': self.id}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(app.config['SECRET_KEY'])
		try:
			user_id = s.loads(token)['user_id']
		except:
			return None
		return User.query.get(user_id)



	def __repr__(self):
		return "User('{u}','{e}','{i}','{id}','{s}','{t}', '{p}', '{c}', '{s1}', '{d1}', '{m}', '{v}', '{w}', '{m1}')".format(u=self.username, e=self.email, i=self.image_file, id=self.id, s=self.state, t=self.times, p=self.pincode, c=self.contaminated, s1=self.s1 ,d1=self.d1, m=self.med_name, v=self.med_verify, w=self.pin_state, m1=self.med_edit)

