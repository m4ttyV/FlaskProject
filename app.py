from flask import Flask
from structures.views import index

app = Flask(__name__)
app.register_blueprint(index)
