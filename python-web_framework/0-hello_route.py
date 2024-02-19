"""FLASK initialized"""
from flask import Flask

app = Flask(_name_)
"""create route at / display --> “Hello HBNB!”"""
@app.route('/',strict_slashes=False)
def hello():
    
    return "Hello HBNB!"


if _name_ == '_main_':
    '''run flask on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000)