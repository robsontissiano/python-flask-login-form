from flask import Flask, render_template, url_for, redirect
from flask_login import login_user, LoginManager, login_required, logout_user
from flask_bcrypt import Bcrypt

from models.user import db, User
from forms import RegisterForm, LoginForm


app = Flask(__name__)
db.init_app(app)

bcrypt = Bcrypt(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "thisisasecretkey"


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    """Reload the user object from the user id stored in the session"""
    return User.query.get(int(user_id))


@app.route("/")
def home():
    """Main endpoint to home index"""
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Method that logs a user in and handle the login form"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("dashboard"))
    return render_template("login.html", form=form)


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    """Dashboard endpoint to access after login"""
    return render_template("dashboard.html")


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    """Method to log a user out"""
    logout_user()
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    """Method that registers a user and handle the register form"""
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
