# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()
from flask import Flask
from structures.views import index

app = Flask(__name__)

if __name__ == 'main':
  app.run(debug=True)

