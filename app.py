from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def default():
    return jsonify(ok=True, message='Hello, World!')


@app.route('/try-it/')
def try_it():
    return jsonify(ok=True, message='TRY, World!')

@app.route('/api/')
def api():
    return jsonify(ok=True, message='API, World!')

if __name__ == '__main__':
    app.run(debug=True)
