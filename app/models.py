from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    ratings = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.id}>'
