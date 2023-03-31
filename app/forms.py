from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email

class RegisterForm(FlaskForm):
    vendor = SelectField(u' Type of Account', choices=[('vendor', 'vendor'), ('user', 'user')])
    submit = SubmitField('Register')

class UserRegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class RegisterVendorForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    store_name = StringField('Store Name', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    store_type = StringField('Type of Store', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register Vendor')

class SignInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class BoxPostForm(FlaskForm):
    items = TextAreaField('Description of Items', validators=[DataRequired()])
    pickup_time = StringField('Pick-Up Time', validators=[DataRequired()])
    price = StringField('Price per Box', validators=[DataRequired()])
    submit = SubmitField('Post Boxes')

# class AddBox(FlaskForm):
#     user_id = 
#     post_id = 
#     submit = SubmitField('Reserve Box')

