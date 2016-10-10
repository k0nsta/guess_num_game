from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import NumberRange


class NumberForm(FlaskForm):
    number = IntegerField(label='Type your number:', validators=[NumberRange(min=0, max=100,
                                                        message='Out of range. Acceptable range 0 - 100')])
