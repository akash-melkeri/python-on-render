from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def default():
    return jsonify(ok=True, message='Hello, World!')

@app.route('/api/')
def default():
    return jsonify(ok=True, message='API, World!')

if __name__ == '__main__':
    app.run(debug=True)
