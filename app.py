from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = [
            data['age'],
            data['gender'],
            data['ethnicity'],
            data['parental_education'],
            data['study_time_weekly'],
            data['absences'],
            data['tutoring'],
            data['parental_support'],
            data['extracurricular'],
            data['sports'],
            data['music'],
            data['volunteering']
        ]
        
        features_array = np.array([features])
        prediction = model.predict(features_array)
        grade_classes = ['A', 'B', 'C', 'D', 'F']
        result = grade_classes[int(prediction[0])]
        
        return jsonify({'grade_class': result})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
