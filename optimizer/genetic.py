import random
import time
import os
import json

def simulate(generations, popsize):
    for i in range(1, generations+1):
        time.sleep(random.random())
        y = int(i * 100 / generations)
        print("{}%".format(y))
        yield "data:" + str(y) + "\n\n"


def save2json(directory, dictionary):
    path = os.path.join(directory, 'params.json')
    with open(path, 'w+') as outfile:
        json.dump(dictionary, outfile)

def readjson(directory, filename='params.json'):
    path = os.path.join(directory, filename)
    with open(path) as myfile:
        return json.load(myfile)