from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Server Flask jalan"

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'admin' and password == '123':
        return "Login sukses bolo"
    else:
        return "Login gagal bolo"

if __name__ == "__main__":
    app.run(debug=True)
