# Patrick Tighe
# Project: Project 3
# 12/8/17


"""
Project 3

We have been manually drawing the division lines to demonstrate the creation of
k-D trees and quadtrees. These lines are drawn so mechanically that we should
be able to write a Python program to automatically draw these lines for a
given tree. You only need to do this for one type of trees (k-D tree or
quadtree).
"""
import sys
# This line should be replaced with the location of the files detailed in the README file
sys.path.append("D:\\Documents\\School\\AU17\\programming\\lib\gisalgs")

from geom.point import*
from indexing.pointquadtree1 import*
import matplotlib.pyplot as plt
import random
import math


def draw_lines(q, plt, xmin=-100, xmax=100, ymin=-100, ymax=100):
    if((q is None)or q.nw is None and q.ne is None and q.sw is None and q.se is None):
        return  # if the tree being examined is a  node, don't draw anything
##    print("xmin:%f  xmax:%f  ymin:%f  ymax:%f"%(xmin,xmax,ymin,ymax))
    plt.plot([xmin, xmax], [q.point.y, q.point.y],
             'k-', lw=1)  # draws horizontal line
    plt.plot([q.point.x, q.point.x], [ymin, ymax],
             'k-', lw=1)  # draws vertical line
    draw_lines(q.nw, plt, xmin, q.point.x, q.point.y, ymax)  # enter nw tree

    draw_lines(q.ne, plt, q.point.x, xmax, q.point.y, ymax)  # enter ne tree

    draw_lines(q.se, plt, q.point.x, xmax, ymin, q.point.y)  # enter se tree

    draw_lines(q.sw, plt, xmin, q.point.x, ymin, q.point.y)  # enter sw tree
    return


def draw_bounds(linesxy):
    frame = plt.gca()
    line = plt.Line2D(linesxy[0], linesxy[1], color='red')
    frame.add_line(line)


def project3(data):
    # arbitrarily large/small numbers for min/max
    xmax = -123123123123
    xmin = 12312312313
    ymin = 12312313123
    ymax = -1231313212312
    points = [Point(d[0], d[1]) for d in data]  # create points from list
    q = pointquadtree(points)  # make quadtree under variable q
    print("Data list: ", end="")  # show user the points being used
    print([search_pqtree(q, p) for p in points])
    pointsintree = [search_pqtree(q, p) for p in points]
    x = [p.x for p in points]  # extract x and y coords for graphing
    y = [p.y for p in points]
    plt.figure(num=1, figsize=(7, 6))
    plt.scatter(x, y, edgecolor='none',
                facecolor='blue', alpha=1)  # plot points
    for p in points:  # set mins and maxes using p as a temp variable to hold the point
        if(p.x > xmax):
            xmax = p.x
        if(p.x < xmin):
            xmin = p.x
    for p in points:
        if(p.y > ymax):
            ymax = p.y
        if(p.y < ymin):
            ymin = p.y
    xmin -= 2
    xmin = math.ceil(xmin)
    xmax += 2
    xmax = math.ceil(xmax)
    ymin -= 2
    ymin = math.ceil(ymin)
    ymax += 2
    ymax = math.ceil(ymax)
    leftbound = [[xmin, xmin], [ymin, ymax]]
    draw_bounds(leftbound)
    topbound = [[xmin, xmax], [ymax, ymax]]
    draw_bounds(topbound)
    rightbound = [[xmax, xmax], [ymax, ymin]]
    draw_bounds(rightbound)
    botbound = [[xmin, xmax], [ymin, ymin]]
    draw_bounds(botbound)
    draw_lines(q, plt, xmin, xmax, ymin, ymax)  # enter drawing lines function
    plt.title("Order of points graphed: \n" + str(pointsintree), wrap=True)
    plt.show()


for i in range(10):
    # show 10 graphs of 7 points with random float points
    data = [Point(random.random() * 15.0, random.random() * 15)
            for i in range(7)]
    project3(data)
