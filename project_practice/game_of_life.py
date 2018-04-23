#!/usr/bin/env python

import numpy as np
import random, time, sys
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

usage_doc='Usage of script: script_name <size_of_canvas:int>'

choice = [0]*100 + [1]*10
random.shuffle(choice)

def create_canvas(size):
    canvas = [ [False for i in range(size)] for j in range(size)]
    return canvas

def seed(canvas):
    for i,row in enumerate(canvas):
        for j,_ in enumerate(row):
            canvas[i][j]=bool(random.getrandbits(1))

def run(canvas):
    ''' This function runs the rules of game through all points, and changes their status accordingly.(in the same canvas)
    @Args:
    --
    canvas : canvas of popu;ation to ran the rules on.

    @returns:
    --
    None
    '''
    canvas = np.array(canvas)
    next_gen_canvas = np.array(create_canvas(canvas.shape[0]))
    for r, row in enumerate(canvas):
        for c, pt in enumerate(row):
            #print(r-1,r+2,c-1,c+2)
            next_gen_canvas[r][c] = __judge_point(pt,canvas[r-1:r+2,c-1:c+2])

    canvas = next_gen_canvas
    def next_gen_canvas #cleaning memory as we mova on.
    return canvas.tolist()

def __judge_point(pt,neighbours):
    dead = 0
    alive = 0
    #finding dead or alive neighbours count.
    for i in neighbours:
        for status in i:
            if status: alive+=1
            else: dead+=1

    #handling duplicate entry for focus pt.
    if pt : alive-=1
    else : dead-=1

    #running the rules of game here.
    state = pt
    if pt:
        if alive<2:
            state=False
        elif alive==2 or alive==3:
            state=True
        elif alive>3:
            state=False
    else:
        if alive==3:
            state=True

    return state

if __name__=='__main__':
    if len(sys.argv) != 2: raise Exception(usage_doc)

    canvas_size = int(sys.argv[1])
    #main working structure of this module.
    c=create_canvas(canvas_size)
    seed(c)
    fig, ax = plt.subplots()
    fig.show()
    cmap = ListedColormap9['w','k'])
    try:
        while True:
            c = run(c)
            ax.matshow(c,cmap=cmap)
            fig.convas.draw()
            ax.cla()
    except KeyboardInterrupt:
        #do nothing.
        pass

