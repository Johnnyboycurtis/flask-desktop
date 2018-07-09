import random
import time


def simulate(generations, popsize):
    for i in range(1, generations+1):
        time.sleep(random.random())
        y = int(i * 100 / generations)
        print("{}%".format(y))
    #yield y
