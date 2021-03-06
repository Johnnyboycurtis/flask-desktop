from flask import Flask
from flask import render_template, request, send_file, Response
import time

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'ABC123'

from .forms import RegistrationForm, GAParams


'''
Some Demo Views
'''

@app.route('/demo', methods = ['GET', 'POST'])
def demo():
    form = RegistrationForm()
    return render_template('demo/demo.html', form=form, title = "Demo")


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
        time.sleep(0.2)
        yield "data:" + str(x) + "\n\n"

@app.route('/progress')
def progress():
    return Response(generate(), mimetype= 'text/event-stream')


'''
Main App Views
'''

@app.route("/", methods = ["GET", "POST"])
@app.route("/home", methods = ["GET", "POST"])
@app.route("/ga", methods = ["GET", "POST"])
def ga():
    form = GAParams()
    title = "Genetic Algorithm"
    return render_template('ga/ga.html', form=form, title=title)


from . import genetic

@app.route("/results", methods = ["POST"])
def results():
    title = "GA Results"
    generations = int(request.form['generations'])
    popsize = int(request.form['popsize'])
    genetic.simulate(generations, popsize)
    return render_template("ga/results.html", title=title, generations=generations, popsize=popsize)