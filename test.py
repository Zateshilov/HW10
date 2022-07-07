from flask import Flask
import json


app = Flask(__name__)


@app.route("/")
def second_page():
    return "Первая страничка"

app.run()





