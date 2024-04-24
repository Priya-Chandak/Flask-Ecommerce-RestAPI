# flask_tech_stack

# Technologies Used
Python
Flask
SQLAlchemy
SQLite (Database)

# Install Virtualenv using command line
python3 -m venv venv

# Activate Virtualenv using command line
source venv/bin/activate

# Install all necessaary requirements
pip3 install -r requirements.txt


# Run the project by this command -
python3 run.py 

OR

export FLASK_APP=run.py
flask run

# Endpoints - 
1. Get all products

URL: /products
Method: GET
Description: Gives a list of all products.
Response: JSON array of products.

2. Get product by ID
URL: /products/<id>
Method: GET
Description: Give details of a specific product by its ID.
Response: JSON object representing the product.

3. Create a new product
URL: /products
Method: POST
Description: Create a new product with details like name, description, and ratings.
example - 
        {
            "description": "Desc1",
            "name": "Name1",
            "ratings": 4.0
        }

4. Update product by ID
URL: /products/<id>
Method: PUT
Description: Update an existing product based on its ID.
Request Body: JSON object containing updated product details
Response: JSON object with a success message.

example -
        {
            "description": "Desc2",
            "name": "Name2",
            "ratings": 4.0
        }

5. Delete product by ID
URL: /products/<id>
Method: DELETE
Description: Delete a product by its ID.
Response: JSON object with a success message.
