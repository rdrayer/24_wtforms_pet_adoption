from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):

    name = StringField("Pet Name", 
                       validators=[InputRequired()])
    species = SelectField("Species",
                          validators=[InputRequired()],
                          choices=[('dog', 'Dog'), ('cat', 'Cat')])
    photo_url = StringField("Photo URL",
                            validators=[URL(), Optional()])
    age = IntegerField("Age",
                       validators=[NumberRange(min=0, max=30)])
    notes = StringField("Notes")
