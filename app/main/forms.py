from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, InputRequired, Email, IPAddress

class AddBadIP(FlaskForm):
    IPAddr=StringField('IP Address',
        validators=[DataRequired(), IPAddress()]
    )
    host_name=StringField('Hostname', validators=[DataRequired()])
    banReason=StringField('Reason for ban', validators=[DataRequired()])
    submit = SubmitField('Ban IP')
