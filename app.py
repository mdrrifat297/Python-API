from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Load users data from the JSON file
def load_users():
    with open("users.json", "r") as file:
        return json.load(file)

# Routes
@app.route('/api/users', methods=['GET'])
def get_users():
    users = load_users()
    return jsonify(users)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    users = load_users()
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/api/users', methods=['POST'])
def add_user():
    users = load_users()
    new_user = request.get_json()
    
    if not new_user.get('name') or not new_user.get('email') or not new_user.get('age'):
        return jsonify({"error": "Invalid data"}), 400

    new_user['id'] = max(u['id'] for u in users) + 1 if users else 1
    users.append(new_user)

    # Save the updated data back to the JSON file
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)
    
    return jsonify(new_user), 201

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = load_users()
    user = next((u for u in users if u['id'] == user_id), None)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    users = [u for u in users if u['id'] != user_id]
    
    # Save the updated data back to the JSON file
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)
    
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
