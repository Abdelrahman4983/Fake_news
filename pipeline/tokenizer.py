import json
from keras.utils import pad_sequences
from keras.preprocessing.text import tokenizer_from_json

class Tokenizer:
    def __init__(self, text, language):
        self.text = [text]
        self.language = language

        if self.language == 'EN':
            self.max_length = 200
        elif self.language == 'AR':
              self.max_length = 150
        self.trunc_type = 'post'
        self.padding_type = 'post'
        self.tokenizer = self.load_data()
        self.text = self.tokenize()
        self.text = self.padding()
        return None
    
    def load_data(self):
        if self.language == 'EN' :
            with open('tokenizers_conf/tok_conf_en.json') as json_file:
                self.tokenizer = tokenizer_from_json(json.load(json_file))
        elif self.language == 'AR' :
            with open('tokenizers_conf/tok_conf_ar.json') as json_file:
                self.tokenizer = tokenizer_from_json(json.load(json_file))
        return self.tokenizer
    
    def tokenize(self):
        self.text = self.tokenizer.texts_to_sequences(self.text)
        return self.text
    
    def padding(self):
        self.text = pad_sequences(self.text, maxlen=self.max_length,
                         padding=self.padding_type,
                         truncating=self.trunc_type)
        return self.text
