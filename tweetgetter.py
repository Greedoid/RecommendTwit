from flask.ext.wtf import Form
from wtforms import TextField
from wtforms import SubmitField
from wtforms.validators import Required

class TweetForm(Form): #Simple form to throw into the HTML
	handle = TextField('handle', validators = [Required()])
	submit = SubmitField('Submit')
