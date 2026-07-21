import numpy as np

from app.services.embedding_service import EmbeddingService


text1 = "Python is a programming language."

text2 = "Python is used for software development."

text3 = "I love eating pizza."


embedding1 = EmbeddingService.generate_embedding(text1)
embedding2 = EmbeddingService.generate_embedding(text2)
embedding3 = EmbeddingService.generate_embedding(text3)


vector1 = np.array(embedding1)
vector2 = np.array(embedding2)
vector3 = np.array(embedding3)


# -------------------------
# Cosine Similarity
# -------------------------

def cosine_similarity(a, b):

    return np.dot(a, b) / (
        np.linalg.norm(a) *
        np.linalg.norm(b)
    )


# -------------------------
# Dot Product
# -------------------------

def dot_product(a, b):

    return np.dot(a, b)


# -------------------------
# Euclidean Distance
# -------------------------

def euclidean_distance(a, b):

    return np.linalg.norm(a - b)


print("=" * 60)

print("Sentence 1")
print(text1)

print("\nSentence 2")
print(text2)

print("\nCosine Similarity")
print(cosine_similarity(vector1, vector2))

print("\nDot Product")
print(dot_product(vector1, vector2))

print("\nEuclidean Distance")
print(euclidean_distance(vector1, vector2))

print("=" * 60)

print("Sentence 1")
print(text1)

print("\nSentence 3")
print(text3)

print("\nCosine Similarity")
print(cosine_similarity(vector1, vector3))

print("\nDot Product")
print(dot_product(vector1, vector3))

print("\nEuclidean Distance")
print(euclidean_distance(vector1, vector3))

print("=" * 60)