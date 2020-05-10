from flask import Flask, render_template, request, redirect, url_for
import pythonYoutube

app = Flask(__name__)             # create an app instance


@app.route("/")                   # at the end point /
def index():                      # call method hello
    return render_template("index.html")


@app.route('/', methods=['POST'])
def index_post():
    link = request.form['link']
    print(link, ' LINK!!!')
    return redirect(url_for('submitted'))


@app.route('/submitted')
def submitted():
    return render_template("submitted.html")


if __name__ == '__main__':
    app.run(debug=True)
