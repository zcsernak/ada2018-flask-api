# Small Flask api
In this repository you can find a small python script ([*ADA_FLASK.py*](ADA_FLASK.py)) which will create an api on your localhost.  
The script loads 2 ml models: a [linear](linear.model) and a [random forest](randomforest.model) one. They have been trained on a very small set of data consisting of real estate features (*area, number of rooms, price*).  

### Requirements
Install the [requirements](requirements.txt) with pip:  
``pip install -r requirements.txt``  
(I suggest to make a [virtualenv](https://virtualenv.pypa.io/en/latest/) for it.)

### Running the script
Issue the following command:
``python ADA_FLASK.py``

### Testing
You can test the script by making requests to the api:  
- linear model is located at ``/api/v1.0/linear``
- random forest is located at ``/api/v1.0/random``

Here's an example which will make a request to the api to return the random forest's predicted price of a house which has 4 rooms and its area is 40m<sup>2</sup>:  
``http://localhost:5000/api/v1.0/random?p=40 4``

You can also run the test script: ``python test_api.py``



##### ADA 2018/1 9. kisházi
