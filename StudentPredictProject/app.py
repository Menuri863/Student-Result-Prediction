from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        
        f1 = float(request.form['attendance'])
        f2 = float(request.form['assignment'])
        f3 = float(request.form['quiz_marks'])
        f4 = float(request.form['mid_exam'])
        
        values = [f1, f2, f3, f4]
        prediction = model.predict([values])
        
        return render_template("index.html", prediction=prediction[0])
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)