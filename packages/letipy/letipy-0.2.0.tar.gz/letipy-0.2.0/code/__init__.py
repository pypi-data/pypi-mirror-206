# This is a powerful scientific strings-processing called "StiPy"

import numpy as np
import re
import os
from afinn import Afinn
import nltk
import gmpy2
import afinn

def arrex(words):
    """
    Convert a string or list of strings to a numerical representation using a numpy array.
    """
    if isinstance(words, str):
        words = [words]
    result = []
    for word in words:
        num_list = []
        for letter in word.lower():
            if letter.isalpha():
                num_list.append(ord(letter) - ord('a') + 1)
        result.append(np.array(num_list))
    if len(result) == 1:
        return result[0]
    return np.array(result)


def tokenize(text):
    """
    Tokenize text into individual words or phrases.
    """
    tokens = re.findall(r'\b\w+\b', text)
    return tokens

def normtxt(text):
    """
    Normalize text by converting it to lowercase, removing punctuation marks, and expanding contractions.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"n't", " not", text)
    text = re.sub(r"'re", " are", text)
    text = re.sub(r"'s", " is", text)
    text = re.sub(r"'d", " would", text)
    text = re.sub(r"'ll", " will", text)
    text = re.sub(r"'t", " not", text)
    text = re.sub(r"'ve", " have", text)
    text = re.sub(r"'m", " am", text)
    return text

def tag(sentence):
    """
    Identify the parts of speech of each word in a sentence.
    """
    # Define a list of part of speech tags and a dictionary to map tags to their index in the list
    pos_tags = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP',
                'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB',
                'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']
    pos_dict = {tag: i for i, tag in enumerate(pos_tags)}

    # Tokenize the sentence and extract its part of speech tags
    words = re.findall(r'\b\w+\b', sentence)
    pos_tags = np.zeros(len(words))
    for i, word in enumerate(words):
        pos_tags[i] = pos_dict.get(word, pos_dict['NN'])

    return pos_tags

def namedent(text, file_name):
    with open(file_name, "r") as f:
        names = f.read().splitlines()
    pattern = re.compile(r"\b(" + "|".join(names) + r")\b", re.IGNORECASE)
    matches = re.findall(pattern, text)
    return list(set(matches))

def deword(words, stopwords):
    """
    Remove stopwords from a string or list of strings.
    """
    if isinstance(words, str):
        words = [words]
    if isinstance(stopwords, str):
        stopwords = [stopwords]
    result = []
    for word in words:
        tokens = re.findall(r'\b\w+\b', word)
        filtered = [token for token in tokens if not token in stopwords]
        result.append(" ".join(filtered))
    if len(result) == 1:
        return result[0]
    return result

def encoded(words, encoding="@#$_&-+()/?!;:'\"*~`|•√Π¶∆£€¥¢^°{}\\][℅,"):
    """
    Remove encoded characters from a string or list of strings.
    """
    if isinstance(words, str):
        words = [words]
    result = []
    for word in words:
        for enc in encoding:
            word = word.replace(enc, '')
        result.append(word)
    if len(result) == 1:
        return result[0]
    return result

def sentim(text):
    """
    Determine the sentiment of a text, whether it is positive, negative, or neutral.
    """
    afinn = Afinn()
    sentiment_score = afinn.score(text)
    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    else:
        return 'neutral'

def semantic(str1, str2):
    """
    Computes the semantic similarity between two strings using the bag of words
    model and cosine similarity.
    
    Args:
    str1 (str): First string to compare
    str2 (str): Second string to compare
    
    Returns:
    float: Similarity score between 0 and 1, where 1 indicates identical strings.
    """

# Tokenize the input strings
    tokens1 = re.findall(r"[a-z]+", str1.lower())
    tokens2 = re.findall(r"[a-z]+", str2.lower())

    # Compute the bag of words vectors for the two strings
    vocab = sorted(set(tokens1 + tokens2))
    vec1 = np.array([tokens1.count(word) for word in vocab])
    vec2 = np.array([tokens2.count(word) for word in vocab])

    # Compute the cosine similarity between the two vectors
    similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    return similarity

def deepfind(text1, text2):
    """
    Finds common words or letters in two input texts.

    Args:
    text1 (str): First input text
    text2 (str): Second input text

    Returns:
    list: List of common words or letters
    """

    # Convert the input texts to lowercase
    text1 = text1
    text2 = text2

    # Tokenize the input texts
    tokens1 = re.findall(r"[a-z]+", text1)
    tokens2 = re.findall(r"[a-z]+", text2)

    # Convert the tokens to lowercase
    tokens1 = [token.lower() for token in tokens1]
    tokens2 = [token.lower() for token in tokens2]

    # Find common words or letters using sets and regular expressions
    common_words = set(tokens1) & set(tokens2)
    common_letters = set(re.sub('[^a-z]', '', text1)) & set(re.sub('[^a-z]', '', text2))

    # Convert the common words and letters to lowercase
    common_words = [word.lower() for word in common_words]
    common_letters = [letter.lower() for letter in common_letters]

    # Combine the common words and letters into a single list and sort it
    common_words_letters = list(set(common_words + common_letters))
    common_words_letters.sort()

    return common_words_letters

def netm(str_list):
    # Define stopwords
    my_stopwords = ['the', 'and', 'to', 'of', 'in', 'a', 'that', 'it', 'for', 'with', 'on', 'at', 'by', 'is', 'this', 'there']
    
    # Tokenize, remove stopwords and lemmatize the documents
    docs = []
    for doc in str_list:
        doc_tokens = [word.lower() for word in re.findall(r"[a-z]+", doc) if re.match(r'[a-zA-Z]+', word) and word.lower() not in my_stopwords]
        docs.append(doc_tokens)
    
    # Create a vocabulary
    all_words = [word for doc in docs for word in doc]
    vocab = list(set(all_words))
    
    # Create a matrix of word counts
    doc_word_matrix = np.zeros((len(docs), len(vocab)))
    for i, doc in enumerate(docs):
        for j, word in enumerate(vocab):
            doc_word_matrix[i, j] = doc.count(word)
    
    # Initialize topic matrix randomly
    num_topics = 10
    topic_word_matrix = np.random.rand(num_topics, len(vocab))
    
    # Iterate to find optimal topic matrix
    num_iterations = 100
    for iteration in range(num_iterations):
        doc_topic_matrix = np.dot(doc_word_matrix, topic_word_matrix.T)
        topic_word_matrix *= np.dot(doc_topic_matrix.T, doc_word_matrix) / np.dot(np.dot(topic_word_matrix, doc_word_matrix.T), doc_word_matrix)
    
    # Return the topic matrix
    return topic_word_matrix