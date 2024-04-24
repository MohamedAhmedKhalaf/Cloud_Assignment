import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string


nltk.download("stopwords")
nltk.download('punkt')

# Read text file
text_file = open('paragraphs.txt', 'r')
text = text_file.read()
text_file.close()

# Split the text into words
word_tokens = word_tokenize(text)

# lowering each word
lowered_words = [word.lower() for word in word_tokens]

# setting it to english
stop_words = set(stopwords.words("english"))
punctuation = set(string.punctuation)

# Filter out stopwords
filtered_words = [word for word in lowered_words if word not in stop_words and word not in punctuation]


# freq of each word using counter
freq_word = Counter(filtered_words)
print(freq_word)

# Join back the filtered text
filtered_text = ' '.join(filtered_words)
# print(filtered_text)


