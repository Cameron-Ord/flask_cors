#importing
import json
from flask import Flask,request, make_response, jsonify
import dbhelper, api_helper, dbcreds
import flask_cors
app = Flask(__name__)

@app.post('/api/insert_painting')
#function gets called on api request
def insert_painting():
   try:
      #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.json, ['artist', 'image_url', 'name']) 
         if(error !=None):
            return make_response(jsonify(error), 400)
         #calls the proceedure to insert sent information into the DB
         results = dbhelper.run_proceedure('CALL insert_painting(?,?,?)', [request.json.get('artist'), request.json.get('image_url'), request.json.get('name')])
         #returns results from db run_proceedure
         if(type(results) == list):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify('something has gone wrong'), 500)

   except TypeError:
      print('Invalid entry, try again')
      
   except: 
      print('something went wrong')

#running @app

if(dbcreds.production_mode == True):
   print()
   print('----Running in Production Mode----')
   print()
   app.run(debug=True)
else:
   from flask_cors import CORS
   CORS(app)
   print()
   print('----Running in Testing Mode----')
   print()
   app.run(debug=True)
   
