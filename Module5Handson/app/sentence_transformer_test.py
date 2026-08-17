from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


sentences = [

    "Employees are eligible for annual leave.",

    "Employees can take twenty days of vacation.",

    "Employees can work remotely two days a week.",

    "The company provides medical insurance."

]


embeddings = model.encode(sentences)


print("\n========== EMBEDDING INFORMATION ==========")

print("Number of sentences :", len(sentences))
print("Embedding dimension :", embeddings.shape[1])

print("\n========== SENTENCES ==========")

for index, sentence in enumerate(sentences):

    print(f"{index + 1}. {sentence}")


print("\n========== SIMILARITY ==========")

similarity = cosine_similarity(embeddings)


for i in range(len(sentences)):

    for j in range(i + 1, len(sentences)):

        print(
            f"{i + 1} <-> {j + 1} : "
            f"{similarity[i][j]:.4f}"
        )