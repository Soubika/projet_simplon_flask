#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def text_box():
    texte = request.form['text']
    processed_text = texte.upper()
    return render_template("bienvenue.html" , message = processed_text )

@app.route("/next")
def suite():
    return render_template("page_suivante.html")

if __name__ == "__main__":
    app.run()


