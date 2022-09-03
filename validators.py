from wtforms.validators import InputRequired, Length

user_validator = [InputRequired(), Length(min=4, max=20)]
password_validator = [InputRequired(), Length(min=8, max=20)]
