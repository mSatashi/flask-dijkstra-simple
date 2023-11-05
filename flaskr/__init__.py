import os
from flask import Flask, render_template, request
from . import dijkstra_algorithm as da
from collections import deque

INFINITY = float("inf")

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
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

    return app