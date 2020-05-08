from flask import Flask,render_template_string

app=Flask(__name__)
@app.route('/')
def index():
    return ("Hello World")