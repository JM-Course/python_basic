"""
pip install Flask==1.0.3
"""
from flask import Flask, render_template, request
import logging

app = Flask(__name__)

app.config['LOGGING_LEVEL'] = logging.DEBUG
app.config['LOGGING_FORMAT'] = '%(asctime)s %(levelname)s: %(message)s in %(filename)s:%(lineno)d]'
app.config['LOGGING_LOCATION'] = '../'
app.config['LOGGING_FILENAME'] = 'blog4me.log'
app.config['LOGGING_MAX_BYTES'] = 100000
app.config['LOGGING_BACKUP_COUNT'] = 1000


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/main', methods=['GET'])
def main():
    return render_template("main.html")


@app.route('/second', methods=['GET'])
def second():
    return render_template("second.html")


if __name__ == "__main__":
    app.run()
