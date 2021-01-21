#!/usr/bin/python3
""" display message module """


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def session(exception):
    """ control the log-in and log-out
    of every request
    """
    storage.close()



@app.route('/hbnb_filters', strict_slashes=False)
def display_states():
    """ function display a html
    with a list of states
    """
    all_state = storage.all(State)
    ameniti = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', all_state=all_state, ameniti=ameniti)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
