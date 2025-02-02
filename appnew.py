import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import numpy as np
import os

# Load pre-trained phishing detection model
try:
    with open("phishing_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    messagebox.showerror("Error", "Phishing model not found. Please train the model first.")
    exit(1)

# Feature extraction for URLs
def extract_features(url):
    features = []
    features.append(len(url))  # URL length
    features.append(url.count("."))  # Number of dots
    features.append(url.count("-"))  # Number of hyphens
    features.append(url.count("@"))  # Number of @ symbols
    features.append(url.count("?"))  # Number of ? symbols
    features.append(url.count("="))  # Number of = symbols
    return np.array(features).reshape(1, -1)

# Phishing detection function
def detect_phishing():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    # Check URL
    url_features = extract_features(url)
    url_prediction = model.predict(url_features)[0]

    if url_prediction == 1:
        result = "Phishing URL detected!"
        color = "red"
        phishing_count.set(phishing_count.get() + 1)
    else:
        result = "URL is safe."
        color = "green"
        safe_count.set(safe_count.get() + 1)

    # Log the result
    threat_log.insert(tk.END, f"{url}: {result}\n")
    threat_log.tag_add(color, "end-2c linestart", "end-1c lineend")
    threat_log.tag_config(color, foreground=color)
    threat_log.see(tk.END)  # Scroll to the bottom

    # Update statistics
    update_statistics()

    # Show result in a message box
    messagebox.showinfo("Result", result)

# Update statistics
def update_statistics():
    stats_label.config(text=f"Safe URLs: {safe_count.get()} | Phishing URLs: {phishing_count.get()}")

# Clear threat log
def clear_log():
    threat_log.delete(1.0, tk.END)
    safe_count.set(0)
    phishing_count.set(0)
    update_statistics()

# Create the main application window
app = tk.Tk()
app.title("Phishing Detection App")
app.geometry("600x500")
app.configure(bg="#f0f0f0")

# Modern theme
style = ttk.Style()
style.theme_use("clam")

# URL input field
url_label = ttk.Label(app, text="Enter URL:", background="#f0f0f0", font=("Arial", 12))
url_label.pack(pady=10)
url_entry = ttk.Entry(app, width=50, font=("Arial", 12))
url_entry.pack(pady=10)

# Detect button
detect_button = ttk.Button(app, text="Detect Phishing", command=detect_phishing)
detect_button.pack(pady=10)

# Statistics label
safe_count = tk.IntVar(value=0)
phishing_count = tk.IntVar(value=0)
stats_label = ttk.Label(
    app,
    text=f"Safe URLs: {safe_count.get()} | Phishing URLs: {phishing_count.get()}",
    background="#f0f0f0",
    font=("Arial", 12),
)
stats_label.pack(pady=10)

# Threat log
threat_log_label = ttk.Label(app, text="Threat Log:", background="#f0f0f0", font=("Arial", 12))
threat_log_label.pack(pady=10)
threat_log = tk.Text(app, height=15, width=70, font=("Arial", 12))
threat_log.pack(pady=10)

# Clear log button
clear_button = ttk.Button(app, text="Clear Log", command=clear_log)
clear_button.pack(pady=10)

# Run the application
app.mainloop()