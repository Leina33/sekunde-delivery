from flask_wtf import FlaskForm
from wtforms import TextField,TextAreaField,SubmitField
from wtforms.validators import Required

class ContactForm(Form):
    name = TextField("Name")
    email = TextField("Email")
    subject = TextField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")
