from flask import Flask, render_template, request
import pickle

# Load the pre-trained model and vectorizer
model = pickle.load(open('spamclassifier_MNB.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

app = Flask(__name__)

# Home route - renders the input page
@app.route('/')
def home():
    return render_template('index.html')

# Output route - renders the output page
@app.route('/output')
def output():
    return render_template('output.html', prediction=None)

# Prediction route - processes the input and returns a result
@app.route("/predict", methods=['POST'])
def predict():
    try:
        if request.method == "POST":
            # Get the message from the form
            messg = str(request.form['messg'])

            # Transform the input using the loaded vectorizer
            transformed = vectorizer.transform([messg])
            transformed_data = transformed.toarray()

            # Predict using the loaded model
            pred = model.predict(transformed_data)
            output = str(pred[0])

            # Return the output page with the prediction result
            return render_template('output.html', prediction=f'This email is classified as: {output}')
    except Exception as e:
        return render_template('output.html', prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
