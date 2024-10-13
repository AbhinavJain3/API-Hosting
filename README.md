Here's the updated README file for your **FaceSquare** project, integrating the steps for hosting the model on the company's server:

---

# FaceSquare

## About

FaceSquare is a face detection model that can be accessed via an API. This project allows users to receive input data in the form of images, enabling efficient face detection and analysis. The API functionality has been thoroughly tested and verified using tools like Postman.

## Features

- **Face Detection**: Accurately detects faces in images.
- **API Access**: Easily integrates with various applications via a RESTful API.
- **Image Input**: Supports various image formats as input.
- **Testing with Postman**: Comprehensive testing of API endpoints for reliability and performance.

## Technologies Used

- **Python**: The primary programming language for the face detection model.
- **OpenCV**: For image processing and face detection functionalities.
- **Flask**: Framework for creating the API.
- **Postman**: For testing the API endpoints.
- **NumPy**: For numerical operations on image data.

## Installation

To get started with FaceSquare, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/FaceSquare.git
   cd FaceSquare
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Hosting the Model on the Company's Server

Follow these steps to host the FaceSquare model on the company's server:

### Step 1: Open the Company's Server

Open the command prompt and connect to the server using specific credentials:

```bash
ssh *.*.*.* -p 17777
```
Enter the passcode when prompted.

### Step 2: Open Jupyter Notebook

Use port forwarding to run the Flask server locally.

### Step 3: Install Necessary Dependencies

Run the following command to install Flask:

```bash
pip install flask
```

### Step 4: Create `app.py` File

Create an `app.py` file for hosting the Flask server with the port number set to 8000.

### Step 5: Build the Face Detection Model

Develop the face detection model and import it into the `app.py` file.

### Step 6: Run the `app.py` File

Execute the following command in the terminal:

```bash
python app.py
```

### Step 7: Ensure Correct Directory

Make sure you are in the same directory in the terminal where the `app.py` file is located.

### Step 8: Access the Server URL

Copy the server URL provided in the terminal and paste it into Postman.

### Step 9: Make the HTTP Request

Set the request type to `POST`.

### Step 10: Set Content-Type Header

In the header section, add the following:

- **Key**: `Content-Type`
- **Value**: `application/json`

### Step 11: Add the Image File

In the Body tab, add the file name, change the type to `file`, and select the image on which you want the face detection model to perform.

### Step 12: View the Output

You will see the face dimensions listed under the "faces" column in the response.

### Step 13: Output Example

Here is a sample output:

```json
{
  "faces": [
    {
      "coordinates": {
        "x": 100,
        "y": 150,
        "width": 50,
        "height": 50
      }
    }
  ],
  "status": "success"
}
```


## Here is the given output.<br>
<img src="https://github.com/AbhinavJain3/API-Hosting/assets/118631182/11be1310-f974-4cda-801b-37ab0adcc7a9" width="350">
