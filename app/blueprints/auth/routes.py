from . import bp as auth_bp
from app.forms import RegisterForm, SignInForm, RegisterVendorForm, UserRegisterForm 
from app.blueprints.social.models import User
from flask import render_template, redirect, flash
from flask_login import login_user, logout_user, login_required

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    vendor_form = RegisterVendorForm()
    user_register_form = UserRegisterForm()
    if form.validate_on_submit():
        if form.vendor.data == "vendor":
            return render_template('register_vendor.jinja', vendor_form=vendor_form)
        if form.vendor.data == "user":
            return render_template('user_register.jinja', user_register_form=user_register_form)
    if vendor_form.validate_on_submit():
        vendor = "vendor"
        username = vendor_form.username.data
        email = vendor_form.email.data
        store_name = vendor_form.store_name.data
        first_name = vendor_form.first_name.data
        last_name = vendor_form.last_name.data
        store_type = vendor_form.store_type.data
        password = vendor_form.password.data
        u = User(vendor=vendor, username=username, store_name=store_name, first_name=first_name, last_name=last_name, store_type=store_type, email=email, password_hash=password)
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match:
            flash(f'Username {username} already exists. Try again!')
            return redirect('/register')
        elif email_match:
            flash(f'Email {email} already exists. Try again!')
            return redirect('/register')
        else:
            u.hash_password(password)
            u.commit()
            flash(f'Request to register {username} successful.')
            return redirect('/') 
    if user_register_form.validate_on_submit():
        vendor = "user"
        username = user_register_form.username.data
        email = user_register_form.email.data
        password = user_register_form.password.data
        u = User(vendor=vendor,username=username, email=email, password_hash=password)
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match:
            flash(f'Username {username} already exists. Try again!')
            return redirect('/register')
        elif email_match:
            flash(f'Email {email} already exists. Try again!')
            return redirect('/register')
        else:
            u.hash_password(password)
            u.commit()
            flash(f'Request to register {username} successful.')
            return redirect('/') 
    return render_template('register.jinja', register_form=form)

@auth_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_match = User.query.filter_by(username=username).first()
        if not user_match or not user_match.check_password(password):
            flash(f'Username and/or password does not exist. Please try again!')
            return redirect('/signin')
        flash(f'{username} successfully signed in!')
        login_user(user_match, remember=form.remember_me.data)
        return redirect('/')
    return render_template('signin.jinja', signin_form=form)

@auth_bp.route('/signout')
@login_required
def sign_out():
    logout_user()
    return redirect('/')

