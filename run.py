from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# It will configure and initialize the database connection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

# Product Model - For creating a table in database
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    ratings = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.id}>'

# Routes 

#1. To get all the products -
@app.route('/products', methods=['GET'])
def get_products():
    # query for getting all the products
    products = Product.query.all()
    output = []
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'ratings': product.ratings
        }
        output.append(product_data)
    # jsonify is used to view output in json format
    return jsonify({'products': output})


# Get products by particular id
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    product_data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'ratings': product.ratings
    }
    return jsonify(product_data)


# Post the product with appropriate fields
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(name=data['name'], description=data['description'], ratings=data['ratings'])
    db.session.add(new_product)   #This line adds a new record to the database session
    db.session.commit()   # This line commits the changes made in the current session to the database. 
    return jsonify({'message': 'Product created successfully!'})

# Update the product by id
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    
    '''It tries to fetch an object by its primary key. 
    If the object with the specified ID exists in the database, 
    it returns that object. However, if no object is found with the given ID, 
    it automatically raises a 404 error''' 

    data = request.get_json()
    product.name = data['name']
    product.description = data['description']
    product.ratings = data['ratings']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully!'})

# Delete product by id
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully!'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
