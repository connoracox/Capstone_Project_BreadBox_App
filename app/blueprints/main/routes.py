from . import bp as main_bp
from app.forms import RegisterVendorForm, RegisterForm
from flask import render_template 

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.jinja')

@main_bp.route('/about')
def about():
    return render_template('about.jinja')


