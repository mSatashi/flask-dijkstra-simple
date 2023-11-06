import os
from flask import Flask, render_template, request
from . import dijkstra_algorithm as da
from collections import deque

@app.route('/dijkstra', methods=['GET', 'POST'])
def dijkstra():
    filename = "../flask-project/flaskr/simple_graph.txt"
    graph = da.Graph(filename)
    rd = None
    rp = None

    if request.method == 'POST':
        origin = request.form['origin']
        dest = request.form['dest']
        
        returned_path, returned_distance = graph.shortest_path(origin, dest)
        rp = returned_path
        rd = returned_distance

    return render_template('dijkstra.html', rp = rp, rd = rd)
