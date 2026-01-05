import joblib
import numpy as np
import re
from urllib.parse import urlparse
from flask import Flask, request, jsonify
from flask_cors import CORS
import warnings
import ipaddress

warnings.filterwarnings('ignore', category=UserWarning)

app = Flask(__name__)
CORS(app)

# Load the AI model
MODEL_PATH = 'phishing_model_final.joblib'
model = joblib.load(MODEL_PATH)

class FeatureExtraction:
    def __init__(self, url):
        self.url = url
        try:
            if not re.match(r'^https?://', self.url):
                self.url = "http://" + self.url
            self.parsed_url = urlparse(self.url)
            self.domain = self.parsed_url.netloc
        except Exception:
            self.parsed_url = None
            self.domain = ""

    def getFeaturesList(self):
        # Returns the 8 core features matching the training script
        return [
            self.UsingIP(), self.LongURL(), self.ShortURL(),
            self.Symbol_at(), self.Redirecting_slash(), self.PrefixSuffix_dash(),
            self.SubDomains(), self.HTTPS()
        ]

    def UsingIP(self):
        try:
            ipaddress.ip_address(self.domain)
            return -1 
        except ValueError:
            return 1 

    def LongURL(self):
        return 1 if len(self.url) < 54 else -1

    def ShortURL(self):
        return -1 if re.search(r'bit\.ly|goo\.gl|shorte\.st|tinyurl\.com', self.url) else 1

    def Symbol_at(self):
        return -1 if '@' in self.url else 1

    def Redirecting_slash(self):
        if self.parsed_url and self.parsed_url.path:
            return -1 if '//' in self.parsed_url.path else 1
        return 1

    def PrefixSuffix_dash(self):
        return -1 if '-' in self.domain else 1

    def SubDomains(self):
        dots = self.domain.count('.')
        if dots == 1: return 1
        elif dots == 2: return 0
        return -1

    def HTTPS(self):
        return 1 if self.url.startswith('https://') else -1

@app.route("/")
def home():
    return "<h1>Phishing Detection API Online</h1>"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data.get('url')
    
    # Block non-HTTPS immediately
    if not url.startswith('https://'):
        return jsonify({'prediction': 'PHISHING', 'reason': 'Unencrypted HTTP detected.'})
    
    extractor = FeatureExtraction(url)
    features = np.array(extractor.getFeaturesList())
    prediction = model.predict(features.reshape(1, -1))[0]
    
    if prediction == 1:
        return jsonify({'prediction': 'SAFE', 'reason': 'URL structure verified.'})
    else:
        return jsonify({'prediction': 'PHISHING', 'reason': 'Suspicious pattern detected.'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)