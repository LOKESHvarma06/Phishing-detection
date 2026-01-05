# 🛡️ Phishing Website Detection System

This project is a real-time cybersecurity tool designed to detect phishing websites using **Machine Learning**. It features a **Flask-based backend** for URL analysis and a **Chrome Extension frontend** to provide an immediate safety verdict while browsing.

[Image of a sequence diagram showing a browser extension calling a Flask API for phishing prediction]

---

## 🚀 Features

* **Real-time Prediction**: Analyzes URLs instantly as you visit them.
* **8-Point Feature Extraction**: Checks for critical indicators including IP usage, URL length, shortening services, `@` symbols, redirecting slashes, prefix/suffix dashes, subdomains, and HTTPS status.
* **Machine Learning Powered**: Utilizes a **Gradient Boosting Classifier** for high-accuracy threat detection.
* **Clean Interface**: Provides simple "SAFE" or "PHISHING" indicators with clear reasoning inside the browser popup.

---

## 🛠️ Installation & Setup

### 1. Clone the Project
Open your terminal (Command Prompt or Git Bash) and run the following commands:
```bash
git clone [https://github.com/LOKESHvarma06/Phishing-detection.git](https://github.com/LOKESHvarma06/Phishing-detection.git)
cd Phishing-detection
