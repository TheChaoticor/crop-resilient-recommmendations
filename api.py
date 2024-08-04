from flask import Flask, request, jsonify
from database import add_crop

app = Flask(__name__)

@app.route('/add_crop', methods=['POST'])
def add_new_crop():
    data = request.json
    name = data.get('name')
    soil_type = data.get('soil_type')
    if not name or not soil_type:
        return jsonify({'error': 'Name and soil type are required'}), 400
    add_crop(name, soil_type)
    return jsonify({'message': 'Crop added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
