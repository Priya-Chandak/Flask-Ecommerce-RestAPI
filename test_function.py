import unittest
import json
from run import app, db, Product

class TestAPIEndpoints(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all_products(self):
        # Add test products to the database
        product1 = Product(name='Product 1', description='Description 1', ratings=4.5)
        product2 = Product(name='Product 2', description='Description 2', ratings=3.8)
        db.session.add_all([product1, product2])
        db.session.commit()

        # Test the GET /products endpoint
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data['products']), 2)
        self.assertEqual(data['products'][0]['name'], 'Product 1')
        self.assertEqual(data['products'][1]['name'], 'Product 2')

    def test_get_product(self):
        # Add a test product to the database
        product = Product(name='Test Product', description='Test Description', ratings=4.0)
        db.session.add(product)
        db.session.commit()

        # Test the GET /products/{id} endpoint
        response = self.app.get(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Test Product')
        self.assertEqual(data['description'], 'Test Description')
        self.assertEqual(data['ratings'], 4.0)

    def test_create_product(self):
        # Test the POST /products endpoint
        data = {'name': 'New Product', 'description': None, 'ratings': 3.5}
        response = self.app.post('/products', json=data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Product created successfully!')

    def test_update_product(self):
        # Add a test product to the database
        product = Product(name='Update Product', description='Old Description', ratings=3.0)
        db.session.add(product)
        db.session.commit()

        # Test the PUT /products/{id} endpoint
        data = {'name': 'Updated Product', 'description': 'New Description', 'ratings': 4.0}
        response = self.app.put(f'/products/{product.id}', json=data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        print(data)
        self.assertEqual(data['message'], 'Product updated successfully!')

    def test_delete_product(self):
        # Add a test product to the database
        product = Product(name='Delete Product', description='Delete me', ratings=2.5)
        db.session.add(product)
        db.session.commit()

        # Test the DELETE /products/{id} endpoint
        response = self.app.delete(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Product deleted successfully!')


if __name__ == '__main__':
    unittest.main()
