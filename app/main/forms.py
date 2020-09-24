from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError



class PitchForm(FlaskForm):
	pitch = TextAreaField("Add pitch",validators=[Required()])
	category = RadioField('Label', choices=[('pickup lines','pickup lines'), ('interview pitch','interview pitch'),('product pitch','product pitch'),('promotion pitch','promotion pitch')])
	submit = SubmitField()

class CommentForm(FlaskForm):
	description = TextAreaField('',validators=[Required()])
	submit = SubmitField() 

class UpvoteForm(FlaskForm):
	submit = SubmitField()


class Downvote(FlaskForm):
	submit = SubmitField()
	