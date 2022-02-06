from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from dictionary import histogram, randomWord

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.


@app.route("/")
def home():
    return render_template('index.html', word = randomWord(histogram("./fish.txt")))


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
