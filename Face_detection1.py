
import cv2
import base64
import os
import numpy as np

def detect_faces_haar(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        return {'error': f"Unable to load image from {image_path}"}

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the Haar cascades for face detection
    face_cascade_path = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    # Check if the cascade classifier is loaded successfully
    if face_cascade.empty():
        return {'error': "Unable to load Haar cascade for face detection."}

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Save the image with rectangles drawn around faces in the 'uploads' folder
    uploads_folder = os.path.join(os.getcwd(), 'uploads')
    os.makedirs(uploads_folder, exist_ok=True)

    output_path = os.path.join(uploads_folder, 'output.png')
    cv2.imwrite(output_path, image)

    # Convert the image to base64 for displaying in Flask
    _, img_encoded = cv2.imencode('.png', image)
    img_base64 = base64.b64encode(img_encoded).decode('utf-8')

    # Return information about the detected faces and the path of the saved image
    return {'faces': [{'x': int(x), 'y': int(y), 'width': int(w), 'height': int(h)} for (x, y, w, h) in faces],
            'image_base64': img_base64,
            'saved_image_path': output_path}

# # Example usage:
# image_path = 'path/to/your/image.jpg'
# result = detect_faces_haar(image_path)

# if 'error' in result:
#     print(result['error'])
# else:
#     print(f"Detected faces: {result['faces']}")
#     print(f"Saved image with rectangles drawn around faces: {result['saved_image_path']}")

# # Example usage:
# image_path = 'path/to/your/image.jpg'
# result = detect_faces_haar(image_path)

# if 'error' in result:
#     print(result['error'])
# else:
#     print(f"Detected faces: {result['faces']}")
#     print(f"Saved image with rectangles drawn around faces: {result['saved_image_path']}")

