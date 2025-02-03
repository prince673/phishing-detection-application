# Phishing Detection Desktop App 🛡️

A **Python-based desktop application** for detecting phishing URLs in real-time. This app uses a pre-trained machine learning model to analyze URLs and classify them as **safe** or **phishing**. It features a user-friendly interface, color-coded results, and threat statistics.

---

## Features ✨

- **Real-Time Phishing Detection**:
  - Detects phishing URLs using a pre-trained machine learning model.
- **User-Friendly Interface**:
  - Simple and intuitive GUI built with Tkinter.
- **Color-Coded Results**:
  - Safe URLs are displayed in **green**.
  - Phishing URLs are displayed in **red**.
- **Threat Statistics**:
  - Displays the total number of safe and phishing URLs detected.
- **Clear Log Button**:
  - Allows users to clear the threat log and reset statistics.

---

## Screenshots 📸

### Main Window
![Main Window](screenshots/main_window.png)

### Result
![Result](screenshots/result.png)

---

## Installation 🛠️

### Prerequisites

- Python 3.7 or higher.
- Required Python libraries: `numpy`, `scikit-learn`.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/phishing-detection-app.git
   cd phishing-detection-app

2. Install dependecies:

   pip install -r requiremnt.txt

3. Trainthe model (if phishing_model.pkl is missing):

   pytohn train_model.py

4. Run the app:

   python app.py

Usage 🚀:

1. Enter a URL in the input field.
2. Click Dectect Phishing.
3. The app will:
   Display a message box with the result.
   Log the result in  the threat log with color_coded text.
   update the threat statistics.

File Structure 📂:

phishing-detection-app/
│
├── app.py                # Main application script
├── train_model.py        # Script to train the phishing detection model
├── model/
│   └── phishing_model.pkl  # Pre-trained machine learning model
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
└── screenshots/          # Screenshots for the README

How It Works 🧠:

1. Feature Extraction:
   The app extracts features from the input URL(e.g. length, number of dots, hyphen,s, etc).
2. Model Prediction:
   The Pre-trained model predicts whether the URL is phishing or safe.
3. Result Display:
   The result is displayed in a message box and logged in the threat log.

Acknowledgments 🙏
1. Scikit-learn: This is for providing machine learning tools.
2. Tkinter: For the GUI framework.
3. PhishTank: For providing phishing datasets.
