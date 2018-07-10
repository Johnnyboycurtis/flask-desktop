from flask import Flask
from flask import render_template, request, send_file, Response
import time
import random

app = Flask(__name__)

from .forms import RegistrationForm, GAParams


'''
Some Demo Views
'''
@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
@app.route('/demo', methods = ['GET', 'POST'])
def demo():
    return render_template('demo/demo.html', title = "Demo")


@app.route('/run')
def get_page():
    title = "Running"
    return render_template('progress/progress.html', title=title) # send_file('templates/progress/progress.html')


def generate():
    '''
    Generate data for the EventSource in static/javascript/progress.js
    '''
    x = 0
    while x < 100:
        print(x)
        x = x + 10
        time.sleep(random.random())
        yield "data:" + str(x) + "\n\n"


@app.route('/progress')
def progress():
    return Response(generate(), mimetype= 'text/event-stream')
