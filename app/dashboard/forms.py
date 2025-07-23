from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    description = StringField("What do you want to add to the list?", validators=[DataRequired()])
    submit = SubmitField("Add to list")

    