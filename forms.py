from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError
from validators import user_validator, password_validator
from models.user import User


class RegisterForm(FlaskForm):
    """Form for Register User"""

    username = StringField(
        validators=user_validator, render_kw={"placeholder": "Username"}
    )
    password = PasswordField(
        validators=password_validator, render_kw={"placeholder": "Password"}
    )

    submit = SubmitField("Register")

    def validate_username(self, username):
        """Method to check if user exists"""
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                "That username already exists. Please choose a different one."
            )


class LoginForm(FlaskForm):
    """Form for Log a User in"""

    username = StringField(
        validators=user_validator, render_kw={"placeholder": "Username"}
    )
    password = PasswordField(
        validators=password_validator, render_kw={"placeholder": "Password"}
    )

    submit = SubmitField("Login")
