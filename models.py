"""Models for Cupcake app."""

from email.policy import default
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cupcake(db.Model):
    __tablename__ = "cupcakes"
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    flavor = db.Column(db.Text,nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float,nullable=False)
    image = db.Column(db.Text,nullable=False,default="https://tinyurl.com/demo-cupcake")   

    def to_dict(self):
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }








def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)