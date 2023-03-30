from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendor = db.Column(db.String(64))
    username = db.Column(db.String(64), unique=True, nullable=True)
    store_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    store_type = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(120), nullable=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    # buyer_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    boxesU = db.relationship('UserBoxes', backref='buyerU', lazy='dynamic')   
    def __repr__(self):
        if self.email:
            return f'<User: {self.email}>'
        return f'<User: {self.username}>'
        
    def __str__(self):
        return f'User: {self.email} | {self.username}'
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def commit(self):
        db.session.add(self)
        db.session.commit()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.String(640), nullable=True)
    pickup_time = db.Column(db.String(64), nullable=True)
    price = db.Column(db.String(64), nullable=True)
    buyer = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    boxesP = db.relationship('UserBoxes', backref='buyerP', lazy='dynamic')
    # buyer_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.items}>'

    def commit(self):
        db.session.add(self)
        db.session.commit()

class UserBoxes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))


    def __repr__(self):
        return f'<Post {self.items}>'

    def commit(self):
        db.session.add(self)
        db.session.commit()