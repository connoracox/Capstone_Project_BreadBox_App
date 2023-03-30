from . import bp as social_bp
from .models import User, Post
from app.forms import BoxPostForm, UserRegisterForm
from flask import redirect, render_template, flash, url_for
from flask_login import login_required, current_user
import random

@social_bp.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = BoxPostForm()
    if form.validate_on_submit():

        items = form.items.data
        pickup_time = form.pickup_time.data
        price = form.price.data
        p = Post(items=items, price=price, pickup_time=pickup_time, user_id= current_user.id)
        p.commit()
        flash('Box successfully posted!')
        return redirect(url_for('social.user', username = current_user.username))
    return render_template('post.jinja', post_form=form)

@social_bp.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        redirect('/')
    posts = user_match.posts
    return render_template('user.jinja', user=user_match, posts=posts)

@social_bp.route('/my_boxes', methods=['GET', 'POST'])
def my_boxes(): 
    random
    # post = Post()
    # user = User()
    # user.buyer = current_user
    # print(current_user)
    
    return render_template('my_boxes.jinja', post=post, user=user, random = random) #, buyer=buyer

@social_bp.route('/explore_food', methods=['GET', 'POST'])
def explore_food():
    all_posts = Post.query.all()
    if not all_posts:
        redirect('/')
    posts = all_posts
    return render_template('explore_food.jinja', all_posts=all_posts, posts=posts)

