from application import app
from flask import render_template, redirect, url_for, request
from application.forms import AnimalForm

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='Home')

@app.route('/generate', methods=['GET'])
def generate():
    form = AnimalForm()
    if form.validate_on_submit():
        animalData = Animal(
                the_animal = form.the_animal.data,
                the_noise = form.the_noise.data
                )
    return render_template('home.html', title='Home')
