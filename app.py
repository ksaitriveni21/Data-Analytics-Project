#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request, jsonify
import numpy as np
from joblib import load

app = Flask(__name__)

# Load the trained SVM model
model = load("svm_model.joblib")

# Route to serve the HTML page
@app.route("/")
def home():
    return render_template("index.html")  # Ensure 'index.html' is inside the "templates" folder

# API route for predictions
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)[0]
        return jsonify({"prediction": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




