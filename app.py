from flask import Flask, render_template, request, redirect, url_for, session, send_file
import pythonYoutube
import time
app = Flask(__name__)             # create an app instance
app.secret_key = "prox potato pop potato hot potato give me prox"


@app.route("/")                   # at the end point /
def index():                      # call method hello
    error = None
    return render_template("index.html", value=error)


@app.route('/', methods=['POST'])
def index_post():
    link = request.form['link']
    error = None
    if "https://" in link and "youtube.com" in link:
        session['link'] = link
        return redirect(url_for('submitted'))
    else:
        error = "Invalid Link"
        return render_template('index.html', error=error)


@app.route('/submitted', methods=["GET", "POST"])
def submitted():
    return render_template("submitted.html")


@app.route('/download', methods=["GET", "POST"])
def download():
    done = "Download finished! Should be in your downloads directory"
    link = session.get("link", None)
    pythonYoutube.get_youtube(link)
    return render_template("submitted.html", done=done)



if __name__ == '__main__':
    app.run(debug=True)
