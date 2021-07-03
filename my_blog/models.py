#models.py

from my_blog import db

class User(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    profile_image = db.Column(db.String(20),nullable=False,default='default_profile.png')

class BlogPost():
    pass
