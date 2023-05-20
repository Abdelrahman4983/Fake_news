from pipeline import clean, tokenizer
from keras.models import load_model

class Detector:
    def __init__(self, language):
        self.language = language
        self.model = self.load_model()
        self.results = []
        return None
    
    def load_model(self):
        if self.language == 'EN' :
            model = load_model('models/FakeNewsDetector_en.h5')
        elif self.language == 'AR' :
            model = load_model('models/FakeNewsDetector_ar.h5')
        return model
    

    def predict(self, text):
        clean_text = clean.Clean(text=text, language=self.language).text
        preprocessed_text = tokenizer.Tokenizer(text=clean_text, language=self.language).text
        prediction = self.model.predict(preprocessed_text)
        pred_to_label = {1:'Real', 0:'Fake' }
        return {'language': self.language,'text': text, 'reality_rate': round(prediction[0][0]*100,4), 'label': pred_to_label[round(prediction[0][0])]}
        