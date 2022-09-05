from flask import Flask, render_template, url_for, redirect, abort
from flask_sqlalchemy import SQLAlchemy
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
    messages = []
    message = ''
    status = 200

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                # in case of successful login, render the dashboard
                message = f'User {form.username.data} logged successfully.'
                app.logger.info(message)
                # check how to send message as an argument to redirect
                return redirect(url_for("dashboard"))
            else:
                message = 'Wrong Password'
                app.logger.error(message)
                messages.append(message)
                status = 400
        else:
            message = f'User {form.username.data} not found'
            app.logger.error(message)
            messages.append(message)
            status = 400
    # else:
    #     messages.append('Form invalid')
    #     status = 400

    # In case of form not valid or user not found, or password incorrect,
    # render login template and gets a 400 bad request error
    # return render_template("login.html", form=form, message=messages), 400
    return render_template("login.html", form=form, message=messages), status


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
    messages = []
    message = ''
    status = 200

    user = user = User.query.filter_by(username=form.username.data).first()

    if user:
        status = 400
        message = f'User {form.username.data} already exists.'
        # messages.append(message)
        # return render_template("register.html", form=form, message=messages), status

    if not user and form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)

        try:
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            # in case of successful register, redirect to login
            message = f'User {form.username.data} registered successfully.'
            app.logger.info(message)
            messages.append(message)
            # return redirect(url_for("login", message = messages)), status
            # check how to send message as an argument to redirect
            # return redirect(url_for("login"))
            return render_template("login.html", form=form, message=messages), status
        except NameError:
            status = 400
            message = f'It was not possible to add the user {form.username.data}.'
    # else:
    #     messages.append('Form invalid')
    #     status = 400

    messages.append(message)
    app.logger.error(message)

    return render_template("register.html", form=form, message=messages), status


if __name__ == "__main__":
    app.run(debug=True)
