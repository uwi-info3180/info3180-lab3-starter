from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField
from wtforms.validators import InputRequired


# app = Flask(__name__)
# app.config['SECRET_KEY'] = "nqeuf"

class ContactForm(FlaskForm):
	name = StringField('Name', validators=[InputRequired()])
	email = EmailField('E-mail', validators=[InputRequired()])
	subject = StringField('Subject', validators=[InputRequired()])
	message = TextAreaField('Message', validators=[InputRequired()])



# if __name__ == '__main__':
# 	app.run(debug=True)
