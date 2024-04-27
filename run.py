from app import app, db

if __name__ == '__main__':
    # Create all database tables
    with app.app_context():
        db.create_all()
    # Run the Flask app in debug mode
    app.run(debug=True)
