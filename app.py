from flask import Flask, render_template
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'hello'
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_pets():
    """ Shows list of pets in db """
    pets = Pet.query.all()
    return render_template('list.html', pets=pets)

@app.route( "/" )
def creat_pet():
    return 'yousent your data'

@app.route( '/<int:pet_id>' )
def show_pet(pet_id):
    """ Show details about a single pet """
    pet = Pet.query.get_or_404( pet_id )
    return render_template('details.html', pet=pet)


