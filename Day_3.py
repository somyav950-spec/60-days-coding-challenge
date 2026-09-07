# import nltk
# nltk.download("punkt")
# nltk.download("punkt_tab")
# nltk.download("stopwords")
text = """
Artificial Intelligence is changing the world.
Machine learning helps computers learn from data.
Natural Language Processing helps machines understand human language.
"""

print("Original Text:")
print(text)

import re
tokens = re.findall(r'\b\w+\b',text)

print("\nTokens:",tokens)

# Bag of Words

documents = [
    "Artificial Intelligence is changing the world",
    "Machine learning helps computers learn from data",
    "Natural Language Processing helps machines understand human language"
]

# Create vocabulary
vocabulary = sorted(set(
    word.lower()
    for document in documents
    for word in document.split()
))

print("\nVocabulary:")
print(vocabulary)

# Convert documents into numbers
bag_of_words = []

for document in documents:
    words = document.lower().split()
    vector = [words.count(word) for word in vocabulary]
    bag_of_words.append(vector)

print("\nBag of Words:")
for vector in bag_of_words:
    print(vector)