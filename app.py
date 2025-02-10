from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/home')
def home():
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York',
        'occupation': 'Software Developer',
        'hobbies': ['Reading', 'Traveling', 'Coding']
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)