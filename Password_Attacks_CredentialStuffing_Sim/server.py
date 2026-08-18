from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # This matches the 'letmein' password in your wordlist
    if username == "admin" and password == "letmein":
        return "Welcome admin!", 200
    
    return "Invalid credentials", 401

if __name__ == '__main__':
    app.run(port=5000)
