from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load your trained model
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        print("Received data:", data)  # For debugging

        # Define the feature names used during training (excluding StudentID, GPA, and GradeClass)
        feature_names = [
            'Age', 'Gender', 'Ethnicity', 'ParentalEducation', 'StudyTimeWeekly',
            'Absences', 'Tutoring', 'ParentalSupport', 'Extracurricular', 'Sports',
            'Music', 'Volunteering'
        ]

        # Extract and prepare the features for prediction
        input_features = pd.DataFrame([{
            'Age': data.get('Age'),
            'Gender': data.get('Gender'),
            'Ethnicity': data.get('Ethnicity'),
            'ParentalEducation': data.get('ParentalEducation'),
            'StudyTimeWeekly': data.get('StudyTimeWeekly'),
            'Absences': data.get('Absences'),
            'Tutoring': data.get('Tutoring'),
            'ParentalSupport': data.get('ParentalSupport'),
            'Extracurricular': data.get('Extracurricular'),
            'Sports': data.get('Sports'),
            'Music': data.get('Music'),
            'Volunteering': data.get('Volunteering')
        }], columns=feature_names)

        # Make prediction
        if hasattr(model, 'predict'):
            prediction = model.predict(input_features)
            grade_class = ['A', 'B', 'C', 'D', 'F'][prediction[0]]
            print(prediction)
            return jsonify({'GradeClass': grade_class})
        else:
            return jsonify({'error': 'Model does not have a predict method'}), 500

    except Exception as e:
        # Log the exception for debugging
        print(f'Exception occurred: {e}')
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
