"""Flask app for Cupcakes"""
from crypt import methods
from flask import Flask,jsonify,request,render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

@app.route("/")
def make_home():

    return render_template("home.html")



@app.route("/api/cupcakes")
def all_cupcakes():
    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    
    return jsonify(cupcakes=cupcakes)

@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake=cupcake.to_dict())

@app.route("/api/cupcakes", methods=["POST"])
def add_cupcake():
    data = request.json
    cupcake = Cupcake(
        flavor=data['flavor'],
        size=data['size'],
        rating=data['rating'],
        image=data['image'] or None,
    )
    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.to_dict()), 201)


@app.route("/api/cupcakes/<int:id>", methods=['PATCH'])
def update_cupcake(id):
    data = request.json
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor=data['flavor']
    cupcake.size=data['size']
    cupcake.rating=data['rating']
    cupcake.image=data['image'] or None

    db.session.add(cupcake)
    db.session.commit()
    
    return jsonify(cupcake=cupcake.to_dict())

@app.route("/api/cupcakes/<int:id>", methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")