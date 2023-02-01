from flask import Flask
app = Flask(__name__)
# app = Flask(__name__,
#             static_folder='/path/to/static',
#             template_folder='/path/to/templates')

from views import *

if __name__ == '__main__': 
    app.run()