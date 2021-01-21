#!/usr/bin/python3
""" display message module """


from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def session(exception):
    """ control the log-in and log-out
    of every request
    """
    storage.close()


@app.route('/states/', defaults={'id': ''}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_states(id):
    """ function display a html
    with a list of states
    """
    all_state = storage.all(State)
    return render_template('9-states.html', all_state=all_state, id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
