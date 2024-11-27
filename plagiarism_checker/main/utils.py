import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK stopwords

# Function to preprocess text (lowercase, remove punctuation, remove stopwords)
def preprocess_text(text):
    # Lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenize and remove stopwords
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    
    # Join tokens back into string
    return ' '.join(tokens)

# Function to calculate plagiarism percentage
def calculate_plagiarism(input_text, reference_texts):
    # Preprocess input and reference texts
    processed_input_text = preprocess_text(input_text)
    processed_reference_texts = preprocess_text(reference_texts)
    
    # Add all texts together for vectorization
    all_texts = [processed_input_text] + [processed_reference_texts]
    
    # Vectorize using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # Compute cosine similarity of input text with each reference text
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    
    # Calculate plagiarism percentage as the highest similarity score
    max_similarity = max(similarity_scores[0])
    plagiarism_percentage = max_similarity * 100
    
    return plagiarism_percentage



