from flask_app.models.user import User
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Dashboard
@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        flash("Please log in to access the dashboard.")
        return redirect('/')
    return render_template("dashboard.html")

# Register new user
@app.route('/insert/user', methods=["POST"])
def insert_user():
    if User.reg_validation(request.form):

        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": bcrypt.generate_password_hash(request.form["password"])
        }

        User.insert_user(data)
        return redirect('/')
    return redirect('/')


# Login
@app.route('/login', methods=["POST"])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')

    session['user_id'] = user_in_db.id
   
    return redirect("/dashboard")

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")
