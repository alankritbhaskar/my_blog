# users/views.py
# Required Views - register, login, logout, account, users blog list

from flask import render_template, url_for, flash, redirect,request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from my_blog import db
from my_blog.models import User, BlogPost
from my_blog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from my_blog.users.picture_handler import add_profile_pic

users = Blueprint('users',__name__)

# register
@users.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.seesion.commit()
        flash('Thanks for trusting us! Welcome to MyBlog')
        return redirect(url_for('users.login'))
    
    return render_template('register.html',form=form)


# login

#logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))