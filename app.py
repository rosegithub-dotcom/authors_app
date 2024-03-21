from flask import Flask, jsonify

app = Flask(__name__)

# Sample data representing users
users = [
    {"first_name": "Rose", "last_name": "Mubezi", "email": "234","contact":750303583,"image":"image.jpg","user_type":"author","password":"2786654334"},
    {"first_name": "vivian", "last_name": "Wembazi", "email": "vivianwembazi@gmail.com","contact":73498087,"image":"image.jpg","user_type":"writer","password":"88888888"},
    {"first_name": "Hannah", "last_name": "Wannjiku", "email": "hananny@gmail.com","contact":74008380,"image":"image.jpg","user_type":"developer","password":"33333333"},
    {"first_name": "Angella", "last_name": "kwagala", "email": "kwagala@gmail.com","contact":740067880,"image":"image.jpg","user_type":"admistrator","password":"33333344"},
    {"first_name": "Lumala", "last_name": "Mariam", "email": "lumalamariam@gmail.com","contact":73967523,"image":"image.jpg","user_type":"publisher","password":"33332244"},
]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)









