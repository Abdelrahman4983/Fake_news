from flask import Flask, jsonify, request
from detector import Detector
app = Flask(__name__)

@app.post('/predict')
def predict():
    data = request.json
    try:
        sample = data['text']
        lang = data['language']
    except KeyError:
        return jsonify({'error' : 'No text sent'})
    if lang == 'ar':
        predictions = model_ar.predict(sample)
    else:
        predictions = model_en.predict(sample)

    try:
        result = jsonify(predictions)
    except TypeError as e:
        result = jsonify({'error' : str(e)})
    return result

if __name__ == '__main__':
    model_en = Detector(language='EN')
    model_ar = Detector(language='AR')
    app.run(host='0.0.0.0', debug=True)

