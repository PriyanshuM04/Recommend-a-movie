import pickle
from src.data.load_data import load_raw_data
from src.data.preprocess import preprocess_movies
from src.features.vectorizer import build_similarity_matrix

# Load and preprocess
df = load_raw_data()
clean_df = preprocess_movies(df)

# Vectorize
similarity, vectorizer = build_similarity_matrix(clean_df)

# Save artifacts
with open("models/clean_df.pkl", "wb") as f:
    pickle.dump(clean_df, f)

with open("models/similarity.pkl", "wb") as f:
    pickle.dump(similarity, f)

with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Artifacts saved successfully.")
