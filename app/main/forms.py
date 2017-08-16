from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length

class NameForm(FlaskForm):
    name = StringField('Input your name: ',validators=[DataRequired(),Length(1,10)])
    submit = SubmitField('Submit')