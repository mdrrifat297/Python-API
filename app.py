from flask import Flask, jsonify

app = Flask(__name__)

# ডেমো ডেটাসেট
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 28},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 34},
    {"id": 3, "name": "Alice Johnson", "email": "alice@example.com", "age": 23},
    {"id": 4, "name": "Bob Brown", "email": "bob@example.com", "age": 45},
    {"id": 5, "name": "Emily Davis", "email": "emily@example.com", "age": 30},
    {"id": 6, "name": "Michael Wilson", "email": "michael@example.com", "age": 38},
    {"id": 7, "name": "Sarah Miller", "email": "sarah@example.com", "age": 27},
    {"id": 8, "name": "Chris Anderson", "email": "chris@example.com", "age": 31},
    {"id": 9, "name": "Olivia Thomas", "email": "olivia@example.com", "age": 29},
    {"id": 10, "name": "David Harris", "email": "david@example.com", "age": 40}
]

products = [
    {"id": 1, "name": "Laptop", "price": 1200, "category": "Electronics"},
    {"id": 2, "name": "Smartphone", "price": 800, "category": "Electronics"},
    {"id": 3, "name": "Table", "price": 150, "category": "Furniture"},
    {"id": 4, "name": "Chair", "price": 100, "category": "Furniture"},
    {"id": 5, "name": "Headphones", "price": 200, "category": "Electronics"},
    {"id": 6, "name": "Refrigerator", "price": 1500, "category": "Appliances"},
    {"id": 7, "name": "Microwave", "price": 300, "category": "Appliances"},
    {"id": 8, "name": "Notebook", "price": 10, "category": "Stationery"},
    {"id": 9, "name": "Pen", "price": 2, "category": "Stationery"},
    {"id": 10, "name": "Smartwatch", "price": 250, "category": "Electronics"}
]

orders = [
    {"id": 1, "user_id": 1, "product_id": 2, "quantity": 1, "status": "Shipped"},
    {"id": 2, "user_id": 2, "product_id": 1, "quantity": 1, "status": "Processing"},
    {"id": 3, "user_id": 3, "product_id": 3, "quantity": 2, "status": "Delivered"},
    {"id": 4, "user_id": 4, "product_id": 4, "quantity": 4, "status": "Cancelled"},
    {"id": 5, "user_id": 5, "product_id": 5, "quantity": 1, "status": "Shipped"},
    {"id": 6, "user_id": 1, "product_id": 6, "quantity": 1, "status": "Delivered"},
    {"id": 7, "user_id": 3, "product_id": 7, "quantity": 1, "status": "Processing"},
    {"id": 8, "user_id": 2, "product_id": 8, "quantity": 3, "status": "Delivered"},
    {"id": 9, "user_id": 4, "product_id": 9, "quantity": 5, "status": "Processing"},
    {"id": 10, "user_id": 5, "product_id": 10, "quantity": 1, "status": "Shipped"}
]

# Routes

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    if order:
        return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
