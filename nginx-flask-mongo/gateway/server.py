#!/usr/bin/env python
import os

from flask import Flask, render_template, redirect
from pymongo import MongoClient

from constants import LINKS

app = Flask(__name__)

client = MongoClient("mongo:27017")

@app.route('/')
def gateway_redirect():
    return redirect('/gateway', code=302)

@app.route('/gateway')
def gateway():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    return render_template('index.html', links=LINKS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)

