from random import sample
import sqlite3
from db import db_path
from os import environ
from jinja2 import evalcontextfilter, Markup, escape
from flask import Flask, render_template, request, escape, \
        send_from_directory, g, redirect, url_for

app = Flask(__name__)
zid = environ.get("REMOTE_USER")

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        # handle the submission, display the vote accepted page
        user_input = request.form['num']
        return render_template('index.html', user_input = user_input)
    else:
        # display form
        return render_template('index.html',
                pictures = sample([str(i) for i in range(1,17)], 16))

# example test page
@app.route('/debug')
def debug():
    return "We gotta be sneaky. we gotta be sneaky Charlie, ssneakyyy"

# opens db connection per request
@app.before_request
def before_request():
    g.db = sqlite3.connect(db_path)
    g.db.execute("PRAGMA foreign_keys = 1")

# closes db connection when shutdown
@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

# your css, js, images, and anything that you wouldn't want CGI to execute, but the user
# should see go in the "static" directory during testing During production, it's advisable
# to set this up to be served by apache instead
@app.route('/static/<path:filepath>')
def send_static_file(filepath):
    return send_from_directory('/static', filepath)

if __name__ == '__main__':
    # you should be using this to debug. This allows you to attach an actual debugger to
    # your script, and you can see any errors that occurred in the command line. No pesky
    # log files like cgi does Also note that since use_reloader is on, you shouldn't make
    # changes to the code while the app is paused in a debugger, because it will reload as
    # soon as you hit play again
    app.run(debug=True, use_reloader=True, port=5000)

