from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

# Load the model and scaler
ridge_model = pickle.load(open("models/ridge.pkl", "rb"))
standard_scaler = pickle.load(open("models/scaler.pkl", 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        # Fetching form data
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        # Preprocessing the input
        new_data = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])

        # Making predictions
        result = ridge_model.predict(new_data)

        # Rendering the result
        return render_template('home.html', results=result[0])  # Pass the prediction to the template
    
    # For GET requests, render the form with no result
    return render_template('home.html', results=None)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)
