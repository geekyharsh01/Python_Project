-----------------------------------------Steps to Run the API--------------------------------------------------------------

1)Open terminal in this directory and then install all the requirements on your pc using command - pip install -r requirements.txt 

2)Then move to directory api and then run the api using command -  uvicorn main:app --reload

3)Then it will host the api on the free port on your pc, either do control+click on the link in the terminal or you can copy paste that link in browser.

4) Go to http://127.0.0.1:8000/docs, here link before docs is the link given in your terminal just add /docs ahead of it and you will be directed to FastAPI- Swagger UI
there you can use all the functionalities implemented.

----------------------------------------------------------------------------------------------------------------------------
In the .\api\main.py containes the api endpoints : 
1) POST / detect_cellphone - This end point takes image as input and returns cellular telephone if it contains the cellphone.

2) GET / detected_cellphone - All the predictions that are done by the detect_cellphone endpoints are stored in the list which can be retrieved using this endpoint by inputting the index , if index out of range it will show.

Created a ApiCheck.html, if API server is on then requests can be send throught this webpage and the results can be retrieved from the api.

In the .\api\models.py contains the resnet-50 model which is used to predict the cellphone for the input image.


   
