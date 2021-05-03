from flask import Flask, jsonify, request
import util
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    # print("function called successfully111")
    z = request.data
    z = json.loads(z)
    # total_sqft = float(request.form['total_sqft'])
    # location = request.form['location']
    # bhk = float(request.form['bhk'])
    # bath = float(request.form['bath'])
    total_sqft = float(z['total_sqft'])
    location = z['location']
    bhk = float(z['bhk'])
    bath = float(z['bath'])
    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    return response

if __name__=='__main__':
    print("Starting Python flask server for Home price prediction")
    util.load_data()
    app.run()
