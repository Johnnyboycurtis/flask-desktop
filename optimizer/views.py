from flask import Flask
from flask import render_template, request, send_file, Response
import time

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'ABC123'

from .forms import RegistrationForm


@app.route('/', methods = ['GET', 'POST'])
def home():
    form = RegistrationForm()
    return render_template('home/home.html', form=form)



@app.route('/page')
def get_page():
    return send_file('templates/progress/progress.html')

@app.route('/progress')
def progress():
    def generate():
        x = 0
        while x < 100:
            print(x)
            x = x + 10
            time.sleep(0.2)
            yield "data:" + str(x) + "\n\n"
    return Response(generate(), mimetype= 'text/event-stream')

