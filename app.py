from flask import Flask, render_template, request, redirect, url_for, session, logging
import sys
import pythonYoutube
import os
import json
# import boto3

app = Flask(__name__)             # create an app instance
app.secret_key = "hot potato prox potato"


@app.route("/")                   # at the end point /
def index():                      # call method hello
    error = None
    return render_template("index.html", value=error)


@app.route('/', methods=['POST'])
def index_post():
    link = request.form['link']
    error = None
    if "https://" in link and "youtube.com" in link and "&t=" in link:
        session['link'] = link
        return redirect("http://3.23.209.43/submitted")
    else:
        error = "Invalid Link. Please make sure you provided a timestamp (&t=)"
        return render_template('index.html', error=error)


@app.route('/submitted', methods=["GET", "POST"])
def submitted():
    return render_template("submitted.html", downloadPath=None)


@app.route('/download', methods=["GET", "POST"])
def download():
    link = session.get("link", None)
    downloadPath = pythonYoutube.get_youtube(link)
    done = "Download finished!" + link + downloadPath
    return render_template("submitted.html", done=done, downloadPath=downloadPath)


if __name__ == '__main__':
    app.run()
