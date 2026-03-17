"""
Efuah Akhimien-Mhonan
Lab 11, Introdution to Flask
March 10,2026
"""
from flask import Flask, render_template

"""
create an object from the Flask module
"""
app = Flask(__name__)

# set the routing to the main page 
# 'route' decorator is used to access the root URL
@app.route('/')
def index():
    name = "Prof. Wu"
    fruits = ['apple','orange', 'grapes']
    return render_template('index.html', username = name, listfruits = fruits)

# endpoints refer to the name of the view in the app
@app.route('/about')
def about():
    return '<h1>About us</h1>'

@app.route('/quotes')
def quotes():
    return '<h1>Quotes</h1>'

# set the 'app' to run if you execute the file directly (not when it is imported)
