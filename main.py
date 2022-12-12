"""
This script runs the WbApp application using a development server.
"""
from distutils.log import debug
from os import environ
from WbApp import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '8091'))
    except ValueError:
        PORT = 8091
    app.run(HOST, PORT)
