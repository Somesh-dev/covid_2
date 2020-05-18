from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,NumberRange
from flaskblog.models import User


class RegisterVerifyForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Send link')



	def validate_email(self, email):

		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different email')




class PhoneVerification(FlaskForm):
	phone = IntegerField('Phone no [do not add + or 91]', validators=[NumberRange(6000000000,9999999999)])

	submit = SubmitField(' SEND OTP')

	def validate_phone(self, phone):

		user = User.query.filter_by(phone=phone.data).first()
		if user:
			raise ValidationError('That phone is taken. Please choose a different email')





class RegistrationForm(FlaskForm):
	otp = IntegerField('OTP', validators=[DataRequired()])

	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

	firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])

	lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])

	# phone = IntegerField('Phone no [do not add + or 91]', validators=[DataRequired(), NumberRange(6000000000,9999999999)])

	pincode = IntegerField('Pincode', validators=[DataRequired(), NumberRange(1,900000)])

	pin_state = StringField('State [Try to use sentence case. First letter be Capital and others Small.]', validators=[DataRequired()])

	password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])

	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

	submit = SubmitField('Sign Up')


	def validate_username(self, username):

		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different username')

	# def validate_email(self, email):

	# 	user = User.query.filter_by(email=email.data).first()
	# 	if user:
	# 		raise ValidationError('That email is taken. Please choose a different email')

	




class LoginForm(FlaskForm):

	phone = IntegerField('Phone no [do not add + or 91]', validators=[DataRequired(), NumberRange(6000000000,9999999999)])

	password = PasswordField('Password', validators=[DataRequired()])

	remember = BooleanField('Remember Me')

	submit = SubmitField('Login')


class MedForm(FlaskForm):

	email = StringField('Email [Used to register in the App]', validators=[DataRequired()])

	med_name = StringField('Shop Name', validators=[DataRequired()])

	password = PasswordField('Password [Used to register in the App]', validators=[DataRequired()])

	med_pin = IntegerField('Shop Pin Code', validators=[DataRequired()])

	med_link = StringField('Google map link', validators=[DataRequired()])

	submit = SubmitField('Add Shop')


class VerifyForm(FlaskForm):

	email = StringField('Email [of the shop account]', validators=[DataRequired()])

	submit = SubmitField('Verify Shop')


class RequestResetForm(FlaskForm):

	email = StringField('Email [of the your account]', validators=[DataRequired()])

	submit = SubmitField('Request Password Reset')

	def validate_email(self, email):

		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('That email is not registered.')

class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])

	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

	submit = SubmitField('Reset Password')

class DeleteForm(FlaskForm):

	phone = IntegerField('Phone no [do not add + or 91]', validators=[DataRequired(), NumberRange(6000000000,9999999999)])

	password = PasswordField('Password', validators=[DataRequired()])

	submit = SubmitField('Delete Account')