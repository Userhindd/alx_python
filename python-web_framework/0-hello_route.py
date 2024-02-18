"""
This script demonstrates a basic Flask web application.
"""

# Import necessary module
from flask import Flask

"""
Create a Flask application instance.
"""
app = Flask(_name_)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root path.

    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'

if _name_ == '_main_':
    """
    Main block to run the Flask application.

    Starts the development server on 0.0.0.0:5000.
    """
    app.run(host='0.0.0.0', port=5000)
    