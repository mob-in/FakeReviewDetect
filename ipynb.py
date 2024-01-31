
import warnings, string
warnings.filterwarnings('ignore')

from nltk.corpus import stopwords
import nltk
nltk.download("stopwords")

def text_process(review):
    
    nopunc = [char for char in review if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
