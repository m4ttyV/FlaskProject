from flask import Flask
from structures.views import views

app = Flask(__name__)
app.register_blueprint(views)
