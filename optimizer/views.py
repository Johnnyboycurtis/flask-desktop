from flask import Flask
from flask import render_template, request, send_file, Response
import time
import random

app = Flask(__name__)

from .forms import GAParams

TMP_DIR = '/home/jn107154/Documents/flask-desktop/.tmp/'


'''
Main App Views
'''

@app.route("/")
@app.route("/home")
@app.route("/ga")
def ga():
    form = GAParams()
    title = "Genetic Algorithm"
    return render_template('ga/ga.html', form=form, title=title)


from . import genetic

@app.route("/progress", methods = ["POST"])
def progress():
    title = "GA Results"
    directory = request.form['directory']
    bills = request.form['bills']
    generations = int(request.form['generations'])
    popsize = int(request.form['popsize'])
    project_context = {'title':title, 'directory':directory, 'bills':bills, 'generations':generations, 'popsize':popsize}
    genetic.save2json(TMP_DIR, project_context)
    return render_template("ga/evolve.html", title='Genetic Algorithm')

@app.route("/evolve")
def evolve():
    project_context = genetic.readjson(TMP_DIR, filename='params.json')
    generator = genetic.simulate(project_context['generations'], project_context['popsize'])
    return Response(generator, mimetype= 'text/event-stream')


@app.route("/results")
def results():
    project_context = genetic.readjson(TMP_DIR, filename='params.json')
    return render_template("ga/results.html", title='GA Results', project_context=project_context)
