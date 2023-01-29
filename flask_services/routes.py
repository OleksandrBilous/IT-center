import json
from datetime import datetime
from flask import render_template, redirect, url_for, request, flash
from flask_services import app, db, cb, redis_conection, manager
from flask_services.models import User
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user


@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/services")
@login_required
def services():
    item1 = cb['9b494ecdb35a0c343be2c67a13000724']
    item2 = cb['9b494ecdb35a0c343be2c67a13003623']
    item3 = cb['9b494ecdb35a0c343be2c67a13004093']
    item4 = cb['9b494ecdb35a0c343be2c67a1300452e']
    item5 = cb['9b494ecdb35a0c343be2c67a13005a8c']
    return render_template('services.html',item1=item1,item2=item2, item3=item3, item4=item4,item5=item5)


@app.route("/login", methods = ["GET","POST"])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = User.query.filter_by(login=login).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            dt = datetime.now().timestamp()
            auth_data = {'login_time': dt}
            redis_conection.set(user.login, json.dumps(auth_data))

            next_page = request.args.get('next')

            redirect(next_page)
        else:
            flash('Login or password is not correct')
         

    return render_template('login.html')

@app.route("/register", methods = ["GET","POST"])
def register():
    
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    if request.method == 'POST':
        if not (login or password or password2):
            flash('Please, fill all fields!')
        elif password != password2:
            flash('Passwords are not equal!')
        else:
            hash_pwd = generate_password_hash(password)
            new_user = User(login=login, password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login_page'))
    
    return render_template('register.html')


@app.route("/logout", methods = ["GET", "POST"])
@login_required
def logout():
    auth_data_row = redis_conection.get(current_user.login)
    if auth_data_row:
        auth_data = json.loads(auth_data_row.decode())
        dt = datetime.now().timestamp()
        auth_data['logout_time'] = dt
        redis_conection.set(current_user.login, json.dumps(auth_data))
    logout_user()
    return redirect(url_for('home_page'))

@app.route("/thanks")
def thanks():
    return render_template('thanks.html')

@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)

    return response