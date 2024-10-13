from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from Face_detection1 import detect_faces_haar  # Import your model here
import os

app = Flask(__name__)

# Specify the folder where uploaded images will be stored
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Check if the uploaded file has a valid extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/predict', methods=['POST'])
def predict_route():
    # Check if the POST request has a file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
        

    file = request.files['file']

    # If the user does not select a file, the browser may send an empty file
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
        

    if file and allowed_file(file.filename):
        # Securely save the uploaded file
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        

        # Perform prediction using your model
        result = detect_faces_haar(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        

        # Return the result as JSON
        return jsonify(result)
        
    else:
        return jsonify({'error': 'Invalid file extension'})
        

if __name__ == '__main__':
    
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # Create the 'uploads' folder if it doesn't exist
    app.run(debug=True)

