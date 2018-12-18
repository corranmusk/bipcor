from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, InputRequired, Email, IPAddress

class AddBadIP(FlaskForm):
    badIP=StringField(
        'IP Address',
        validators=[DataRequired(), IPAddress()]
    )
    source=StringField(
        'Detected by IP',
        validators=[DataRequired(), IPAddress()]
    )
    notes=StringField(
        'Reason for ban',
        validators=[DataRequired()]
    )
    submit = SubmitField('Ban IP')
