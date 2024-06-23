from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .forms import LoginForm, RegisterForm
from .models import User
from ..nlp_utils import NovaNLP

nlp = NovaNLP("bert-base-uncased")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("dashboard"))
        flash("Invalid email or password", "danger")
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully", "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/generate_website", methods=["POST"])
@login_required
def generate_website():
    website_data = request.get_json()
    # TO DO: Implement website generation using nlp_utils
    return jsonify({"message": "Website generated successfully"})

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
