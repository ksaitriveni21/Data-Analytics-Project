#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Sai Triveni Kottapalli
# ID - C00313481  


# In[6]:


# HTML & CSS


# In[7]:


from IPython.core.display import display, HTML

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SVM Model Prediction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding: 50px;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            display: inline-block;
        }
        h2 {
            color: #333;
        }
        input {
            padding: 8px;
            margin: 5px;
            width: 80px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            padding: 10px 15px;
            border: none;
            background: #007BFF;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
        p {
            font-size: 18px;
            font-weight: bold;
            margin-top: 10px;
        }
    </style>
    <script>
        async function getPrediction() {
            let features = [
                parseFloat(document.getElementById("f1").value),
                parseFloat(document.getElementById("f2").value),
                parseFloat(document.getElementById("f3").value),
                parseFloat(document.getElementById("f4").value)
            ];

            let response = await fetch("http://127.0.0.1:5000/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ features: features })
            });

            let result = await response.json();
            document.getElementById("output").innerHTML = "Prediction: " + result.prediction;
        }
    </script>
</head>
<body>
    <div class="container">
        <h2>Predict Iris Flower Class</h2>
        <label>Feature 1: <input type="number" id="f1"></label><br>
        <label>Feature 2: <input type="number" id="f2"></label><br>
        <label>Feature 3: <input type="number" id="f3"></label><br>
        <label>Feature 4: <input type="number" id="f4"></label><br>
        <button onclick="getPrediction()">Predict</button>
        <p id="output"></p>
    </div>
</body>
</html>
"""

# Display HTML inside Jupyter Notebook
display(HTML(html_code))

# Save the HTML file
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_code)

print("HTML file 'index.html' saved successfully!")


# In[ ]:




