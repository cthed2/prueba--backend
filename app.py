from flask import Flask, request, jsonify
from flask_cors import CORS  # Importa CORS

app = Flask(__name__)
CORS(app)  # Aplica CORS a la aplicación

@app.route('/')
def hello():
    return "API para recibir datos desde una página web!"

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    if not all([name, email, message]):
        return jsonify({"message": "Todos los campos son requeridos!"}), 400

    with open('data.txt', 'a') as f:
        f.write(f"Name: {name}, Email: {email}, Message: {message}\n")
    
    return jsonify({"message": "Datos almacenados correctamente!"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
