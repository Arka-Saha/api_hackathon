from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    data = request.get_json()

    # Validate JSON structure
    if not data or 'image_url' not in data or 'bounding_box' not in data:
        return jsonify({'error': 'Invalid payload'}), 400

    bounding_box = data['bounding_box']
    required_keys = {'x_min', 'y_min', 'x_max', 'y_max'}
    if not required_keys.issubset(bounding_box.keys()):
        return jsonify({'error': 'Bounding box is missing required keys'}), 400

    # Process the input (for demo purposes, just echoing back)
    response = {
        'message': 'Image processed successfully',
        'image_url': data['image_url'],
        'bounding_box': bounding_box
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
