from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length
class AnimalForm(FlaskForm):
    the_animal = StringField('Animal',
            validators = [
                Length(min=3, max=30)
            ]
    )
    
    the_noise = StringField('Noise',
            validators = [
                Length(min=3, max=30)
            ]
    )
    submit = SubmitField('post')
