from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators
from wtforms.validators import DataRequired, Length

class InputForm(FlaskForm):
    Interface = StringField('Interface Name', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Enter Interface"})
    submit = SubmitField('Submit')