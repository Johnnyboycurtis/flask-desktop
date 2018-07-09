from wtforms import Form, BooleanField, StringField, DateTimeField, validators, FileField, IntegerField

class RegistrationForm(Form):
    username     = StringField('Username', [validators.Length(min=4, max=25)])
    email        = StringField('Email Address', [validators.Length(min=6, max=35)])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])
    birthday  = DateTimeField('Your Birthday', format='%m/%d/%y')



class GAParams(Form):
    generations = IntegerField("Generations", [validators.NumberRange(min=20, max=10000, message="Enter a number between 20 and 10000")], default=20)
    popsize = IntegerField("Population Size", [validators.NumberRange(min=20, max = 10000, message = "Enter a number between 20 and 10000")], default=20)



