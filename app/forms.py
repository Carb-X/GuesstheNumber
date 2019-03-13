from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class GuessNumberForm(FlaskForm):
    number = IntegerField(u'输入一个整数(0~1000)', validators=[
        DataRequired(u'请输入一个有效的整数！'),
        NumberRange(0, 1000, u'请输入0~1000以内的整数！')])
    submit = SubmitField(u'提交')