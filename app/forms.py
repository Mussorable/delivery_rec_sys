from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
from app import db

import sqlalchemy as sa

from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_repeat = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = db.session.scalar(sa.select(User), where=(User.username == username.data))
        
        if user is not None:
            raise ValidationError('Please use a different username.')
        
    def validate_email(self, email):
        user = db.session.scalar(sa.select(User), where=(User.email == email.data))
        
        if user is not None:
            raise ValidationError('This email already exists. Please use another email or Sign In.')
        
class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')