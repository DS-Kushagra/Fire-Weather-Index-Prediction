# Fire Weather Index (FWI) Prediction

A web-based application built using **Flask** that predicts the **Fire Weather Index (FWI)** using a machine learning model. The app accepts weather and environmental parameters as inputs and returns a prediction of the FWI, which helps in assessing wildfire risks.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Input Parameters](#input-parameters)
- [Output](#output)
- [File Structure](#file-structure)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Wildfires are a significant hazard affecting ecosystems and human communities. The **Fire Weather Index (FWI)** is a key component used to assess the potential risk of wildfires based on various environmental and weather conditions. This project leverages machine learning to predict the FWI given a set of weather-related inputs.

The application is simple and intuitive, allowing users to input parameters like temperature, humidity, wind speed, and other related factors to generate predictions.

---

## Features
- User-friendly interface for inputting weather data.
- Real-time predictions powered by a **Ridge Regression** machine learning model.
- Data pre-processing using a **StandardScaler** to normalize inputs.
- Flask-based backend with dynamic HTML templates.
- Easily deployable on any server or cloud platform.

---

## Technologies Used
- **Programming Language**: Python
- **Web Framework**: Flask
- **Machine Learning Model**: Ridge Regression (using scikit-learn)
- **Frontend**: HTML
- **Libraries**: 
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `pickle`
- **Deployment Ready**: Compatible with services like Heroku or AWS.

---

## Installation

Follow these steps to set up and run the application locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fwi-prediction.git
   cd fwi-prediction
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure that the **models** directory contains:
   - `ridge.pkl` (trained Ridge Regression model)
   - `scaler.pkl` (fitted StandardScaler object)

5. Run the Flask application:
   ```bash
   python application.py
   ```

6. Open the application in your browser:
   ```
   http://127.0.0.1:5000
   ```

---

## Usage

1. Navigate to the application in your browser.
2. Enter the required weather parameters in the form fields:
   - Temperature
   - Relative Humidity (RH)
   - Wind Speed (Ws)
   - Rain
   - Fine Fuel Moisture Code (FFMC)
   - Duff Moisture Code (DMC)
   - Initial Spread Index (ISI)
   - Classes
   - Region
3. Click the **Predict** button.
4. View the **Fire Weather Index (FWI)** prediction displayed below the form.

---

## Input Parameters

| Parameter        | Description                              | Example Value |
|------------------|------------------------------------------|---------------|
| `Temperature`    | Air temperature in degrees Celsius       | `22.5`        |
| `RH`             | Relative humidity in percentage          | `45`          |
| `Ws`             | Wind speed in km/h                      | `12.3`        |
| `Rain`           | Rainfall in mm                          | `0.0`         |
| `FFMC`           | Fine Fuel Moisture Code                 | `85.2`        |
| `DMC`            | Duff Moisture Code                      | `45.7`        |
| `ISI`            | Initial Spread Index                    | `4.2`         |
| `Classes`        | Fire classes                            | `1`           |
| `Region`         | Region code                             | `2`           |

---

## Output

The application predicts the **Fire Weather Index (FWI)** as a single numerical value. This index indicates the potential for wildfire occurrence and severity.

---

## File Structure

```
fwi-prediction/
│
├── models/
│   ├── ridge.pkl              # Trained Ridge Regression model
│   ├── scaler.pkl             # Fitted StandardScaler object
│
├── templates/
│   ├── index.html             # Welcome Page
|   ├── home.html              # Main HTML template for the form
│
├── application.py              # Flask application
├── README.md                  # Project documentation
```

---

## Screenshots

### 1. Input Form
![image](https://github.com/user-attachments/assets/92560077-36b1-4228-9aa4-b9132f2dbc7a)

### 2. Prediction Result
![image](https://github.com/user-attachments/assets/5fab23b6-9e5d-43a2-afa5-0c566e4d7254)

---

## Future Enhancements
- Add data visualization to display trends in historical FWI data.
- Improve the UI with better styling and animations.
- Support multiple machine learning models for comparison.
- Deploy the application to a public cloud platform (e.g., Heroku, AWS).
- Add error handling and validation for user inputs.

---

## Contributing

Contributions are welcome! If you have ideas or suggestions for improving the application:
1. Fork this repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push your changes to your forked repository:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request!

