import re
import string
import nltk
from nltk.corpus import stopwords

class Clean:
    def __init__(self, text, language):
        self.text = text
        self.language = language
        if self.language == 'EN':
            self.text = self.clean_english_text()
        elif self.language == 'AR':
            self.text = self.clean_arabic_text()
        
        return None
    
        # Remove Stopwords
    def remove_english_stopwords(self):
        stop_words = stopwords.words('english')
        words = self.text.split()
        filtered_sentence = ''
        for word in words:
            if word not in stop_words:
                filtered_sentence = filtered_sentence + word + ' '
        return filtered_sentence


    # Remove Punvtuation
    def remove_punctuation(self):
        table = str.maketrans('','',string.punctuation)
        words = self.text.split()
        filtered_sentence = ''
        for word in words:
            word = word.translate(table)
            filtered_sentence = filtered_sentence + word + ' '
        return filtered_sentence

    # Normalize Text
    def normalize_english_text(self):
        self.text = self.text.lower()
        # get rid of urls
        self.text = re.sub('https?://\S+|www\.\S+', '', self.text)
        # get rid of non words and extra spaces
        self.text = re.sub('\\W', ' ', self.text)
        self.text = re.sub('\n', '', self.text)
        self.text = re.sub(' +', ' ', self.text)
        self.text = re.sub('^ ', '', self.text)
        self.text = re.sub(' $', '', self.text)
        return self.text


    def normalize_arabic_text(self):
        self.text = re.sub('\\W', ' ', self.text)
        self.text = re.sub('\n', '', self.text)
        self.text = re.sub(r"[إأٱآا]", "ا", self.text)
        self.text = re.sub(r"ى", "ي", self.text)
        self.text = re.sub(r"ؤ", "ء", self.text)
        self.text = re.sub(r"ئ", "ء", self.text)
        self.text = re.sub(r'[^ا-ي ]', "", self.text)

        noise = re.compile(""" ّ    | # Tashdid
                            َ    | # Fatha
                            ً    | # Tanwin Fath
                            ُ    | # Damma
                            ٌ    | # Tanwin Damm
                            ِ    | # Kasra
                            ٍ    | # Tanwin Kasr
                            ْ    | # Sukun
                            ـ     # Tatwil/Kashida
                        """, re.VERBOSE)
        self.text = re.sub(noise, '', self.text)
        return self.text

    # combine all functions into one
    def clean_arabic_text(self):
        self.text = self.text.replace(',',' , ')
        self.text = self.text.replace('.',' . ')
        self.text = self.text.replace('/',' / ')
        self.text = self.text.replace('@',' @ ')
        self.text = self.text.replace('#',' # ')
        self.text = self.text.replace('?',' ? ')
        self.text = self.normalize_arabic_text()
        self.text = self.remove_punctuation()

        return self.text

    def clean_english_text(self):
        self.text = self.text.replace(',',' , ')
        self.text = self.text.replace('.',' . ')
        self.text = self.text.replace('/',' / ')
        self.text = self.text.replace('@',' @ ')
        self.text = self.text.replace('#',' # ')
        self.text = self.text.replace('?',' ? ')
        self.text = self.normalize_english_text()
        self.text = self.remove_punctuation()
        self.text = self.remove_english_stopwords()

        return self.text