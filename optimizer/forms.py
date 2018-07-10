from wtforms import Form, BooleanField, StringField, DateTimeField, validators, FileField, IntegerField

class GAParams(Form):
    directory = StringField('Directory', default='/home/jn107154/Desktop/')
    bills = StringField('Bills File', default='bills.txt')
    generations = IntegerField("Generations", [validators.NumberRange(min=20, max=10000, message="Enter a number between 20 and 10000")], default=20)
    popsize = IntegerField("Population Size", [validators.NumberRange(min=20, max = 10000, message = "Enter a number between 20 and 10000")], default=20)



