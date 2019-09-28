from flask import Flask
from flask_restplus import Api, Resource, reqparse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"