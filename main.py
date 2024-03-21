from flask import Flask, jsonify

app = Flask(__name__)

# Sample data representing users
user = {
     {"first_name": "Angella", "last_name": "kwagala", "email": "kwagala@gmail.com","contact":740067880,"image":"image.jpg","user_type":"admistrator","password":"33333344"},
    
}

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user):
    user = users.get(user)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)