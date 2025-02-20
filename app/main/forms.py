from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, InputRequired, Email, IPAddress


class AddIPAddr(FlaskForm):
    IPAddr = StringField("IP Address", validators=[DataRequired(), IPAddress()])
    source = StringField("Detected by IP", validators=[DataRequired(), IPAddress()])
    notes = StringField("Reason for ban", validators=[DataRequired()])
    submit = SubmitField("Ban IP")


class GenerateToken(FlaskForm):
    tokenIP = StringField(
        "IP Address to use token", validators=[DataRequired(), IPAddress()]
    )
    notes = StringField("Notes",)
    submit = SubmitField("Generate token")


class AddLogEntry(FlaskForm):
    loglevel = StringField("Level of log", validators=[DataRequired()])
    detail = StringField("Log Information", validators=[DataRequired()])
    submit = SubmitField("Add Log Entry")
