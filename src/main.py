import pickle
from src.models.recommender import MovieRecommender

# Load prebuilt artifacts
with open("models/clean_df.pkl", "rb") as f:
    clean_df = pickle.load(f)

with open("models/similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# Initialize recommender
recommender = MovieRecommender(clean_df, similarity)

print(recommender.recommend("Spider-Man"))
