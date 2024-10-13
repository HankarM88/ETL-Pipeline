
import re 
import string
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
# Function to clean the text 
def clean(text):
    if '|' in text:
        text = text.split('|')[1]
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('[^\w\s]', '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text
# Function to preprocess texts 
def preprocess(text): 
    # Get english stops words 
    stop_words = set(stopwords.words("english")) 
    lemmatizer = WordNetLemmatizer()
    # Tokenize text 
    word_tokens = word_tokenize(text) 
    # Remove stop words 
    filtered_text = [word for word in word_tokens if word not in stop_words] 
    #stemming the text 
    preprocessed_text=[lemmatizer.lemmatize(word) for word in filtered_text if len(word)>2]
    # Join text again
    final_text = " ".join(preprocessed_text).strip()
    return final_text