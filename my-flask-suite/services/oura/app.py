#!/usr/bin/env python
import os

from flask import Flask, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongo:27017")

@app.route('/oura')
def oura():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)

