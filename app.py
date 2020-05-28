from flask import Flask, render_template, request, redirect, url_for, session
import pythonYoutube
import os
import sys
from flaskwebgui import FlaskUI
from time import sleep


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


if getattr(sys, 'frozen', False):
    template_folder = resource_path('templates')
    static_folder = resource_path('static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)


# app = Flask(__name__)             # create an app instance
app.secret_key = "hot potato prox potato"
ui = FlaskUI(app)


@app.route("/")                   # at the end point /
def index():                      # call method hello
    error = None
    return render_template("index.html", value=error)


@app.route('/', methods=['POST'])
def index_post():
    link = request.form['link']
    error = None
    if "https://" in link and "you" in link and "?t=" in link:
        session['link'] = link
        return redirect(url_for("submitted"))
    else:
        error = "Invalid Link. Please make sure you provided a timestamp (?t=)"
        return render_template('index.html', error=error)


@app.route('/submitted', methods=["GET", "POST"])
def submitted():
    return render_template("submitted.html")


@app.route('/download', methods=["GET", "POST"])
def download():
    link = session.get("link", None)
    sleep(0.5)
    downloadPath = pythonYoutube.get_youtube(link)
    if downloadPath:
        done = "Download finished! Check your downloads folder"
    else:
        done = "ERROR. TRY AGAIN. PROBABLY SOME BULLSHIT REQUEST DELAY"

    return render_template("submitted.html", done=done)


ui.run()
