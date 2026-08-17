import faiss
import numpy as np


# Vector dimension
dimension = 3


# Create FAISS Index using L2 distance
index = faiss.IndexFlatL2(dimension)


# Sample vectors
vectors = np.array(
    [
        [1.0, 2.0, 3.0],
        [1.1, 2.1, 3.1],
        [5.0, 5.0, 5.0],
        [10.0, 10.0, 10.0],
    ],
    dtype="float32"
)


# Add vectors
index.add(vectors)


print("Total vectors:", index.ntotal)


# Query vector
query = np.array(
    [
        [1.0, 2.0, 3.0]
    ],
    dtype="float32"
)


# Search top 3
distances, indices = index.search(
    query,
    3
)


print("\nDistances:")
print(distances)

print("\nIndices:")
print(indices)