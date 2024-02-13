### This project detects face in the image provided to the model via API.<br>

Here, basically we need to host the model on the Company's server. Below are the steps given for thw same.<br>

<pre>
STEP 1: Open the Company's Server through Command Prompt with the specific credentials.
        Eg: ssh *.*.*.* -p 17777
        Passcode: *******
        
STEP 2: Open jupyter notebook on the server with the help of port forwarding (to run the flask server locally).
        jupyter notebook --no-browser --port=8889
        ssh -N -f -L localhost:8000:localhost:8000 *.*.*.*.* -p 17777

STEP 3: Now install your necessary Dependenies.
        Run `pip install flask`

STEP 4: Make the app.py file for hosting the flask server with port number=8000.

STEP 5: Make the Face Detection Model and import it in the app.py file.

STEP 6: Now, run the app.py file in the Terminal with the following command.
        `python app.py`
  
STEP 7: Make sure you are in the same directory in Terminal where the file app.py is present.

STEP 8: Copy the server URL and paste it in postman.

STEP 9: Make the HTTP request to `POST`.

STEP 10: Now in the header section add `Content Type`:key and `application/json`:value.

STEP 11: In the Body tab, Add the file name, change type to `file` and in the value add the image on which you want the Face Detection Model to perform.

![image](https://github.com/AbhinavJain3/API-Hosting/assets/118631182/73cc3d55-a663-426c-8e39-1be611fdc9b9)


</pre>

        



