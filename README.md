########################################Phishing Website Detection System using Machine Learning########################################
This project is a real-time cybersecurity tool designed to detect phishing websites. 
It uses a Machine Learning backend (Flask) and a Chrome Extension frontend to analyze URL structures and provide an immediate safety verdict.

🚀 Features
Real-time Prediction: Analyzes URLs instantly as you browse.
8-Point Feature Extraction: Checks for IP usage, URL length, shortening services, @ symbols, redirecting slashes, prefix/suffix dashes, subdomains, and HTTPS status.
Machine Learning Powered: Uses a Gradient Boosting Classifier for high-accuracy detection.
Clean Interface: Simple "SAFE" or "PHISHING" status indicators with reasoning.

🛠️ Installation & Setup
1. Clone the Project
Open your terminal and run the following commands to get the code on your machine:

Bash
git clone https://github.com/LOKESHvarma06/Phishing-detection.git
cd your-repo-name
2. Backend Setup (Python)
Ensure you have Python 3.x installed, then set up the backend:

Install Dependencies:
Bash
pip install flask flask-cors joblib scikit-learn pandas numpy


Train the AI Model: Run the training script to generate the phishing_model_final.joblib file from the dataset.

Bash
python train_simple.py
Start the Flask Server: Launch the API that handles requests from the extension.

Bash
python app.py
The server will run at http://127.0.0.1:5000.

3. Chrome Extension Setup
Open Google Chrome and go to chrome://extensions/.

Enable Developer mode using the toggle switch in the top-right corner.
Click the Load unpacked button.

Select the extension/ folder from your project directory.

📁 Project Structure
app.py: The Flask server that performs feature extraction and AI prediction.

train_simple.py: The script used to train the Gradient Boosting model.

phishing.csv: The dataset containing URL features for training.

phishing_model_final.joblib: The saved AI model used by the server.

extension/:

manifest.json: Configuration file for the Chrome extension.

popup.js: Logic to capture the current URL and send it to the backend.

popup.html / popup.css: The layout and styling for the extension UI.

🔍 How it Works
Input: When the user clicks the extension, popup.js captures the active tab's URL.

Request: The extension sends a POST request to the /predict endpoint on the local Flask server.

Analysis: The app.py script extracts 8 structural features from the URL string.

Verdict: The pre-trained ML model processes these features and returns a classification: SAFE or PHISHING.

📝 Requirements
Python 3.8+

Chrome Browser

Libraries: flask, flask-cors, joblib, sklearn, pandas, nump
