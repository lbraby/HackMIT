#!/usr/bin/env python3
# script.py
# Making first text website for tutorial learning purposes

from flask import session, request, redirect, Flask, render_template
import uuid

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home2():
        return redirect("/index.html");

    @app.route('/index.html')
    def home():
        return "<p>Hello, World!</p>"
    return app

app = create_app()
app.run(host="128.199.35.33", port="5000")
