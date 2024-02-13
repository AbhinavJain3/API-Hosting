### This project detects face in the image provided to the model via API.<br>

Here, basically we need to host the model on the Company's server. Below are the steps given for thw same.<br>

<b>STEP 1:</b> Open the Company's Server through Command Prompt with the specific credentials.<br>
<pre>
        Eg: ssh *.*.*.* -p 17777
        Passcode: *******
</pre>        
 
<b>STEP 2:</b> Open jupyter notebook on the server with the help of port forwarding (to run the flask server locally).

<b>STEP 3:</b> Now install your necessary Dependenies.<br>
&nbsp;&emsp;&emsp;&nbsp; Run `pip install flask`

<b>STEP 4:</b> Make the app.py file for hosting the flask server with port number=8000.

<b>STEP 5:</b> Make the Face Detection Model and import it in the app.py file.

<b>STEP 6:</b> Now, run the app.py file in the Terminal with the following command.<br>
&nbsp;&emsp;&emsp;&nbsp;         `python app.py`
  
<b>STEP 7:</b> Make sure you are in the same directory in Terminal where the file app.py is present.

<b>STEP 8:</b> Copy the server URL and paste it in postman.

<b>STEP 9:</b> Make the HTTP request to `POST`.

<b>STEP 10:</b> Now in the header section add `Content Type`:key and `application/json`:value.

<b>STEP 11:</b> In the Body tab, Add the file name, change type to `file` and in the value add the image on which you want the Face Detection Model to perform.

<img  src="https://github.com/AbhinavJain3/API-Hosting/assets/118631182/73cc3d55-a663-426c-8e39-1be611fdc9b9" width="700">

<b>STEP 12:</b> Now, you can see the face dimensions in the below faces column.

<b>STEP 13:</b> Here is the given output.<br>
<img src="https://github.com/AbhinavJain3/API-Hosting/assets/118631182/11be1310-f974-4cda-801b-37ab0adcc7a9" width="350">
