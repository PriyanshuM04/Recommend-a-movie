from src.data.load_data import load_raw_data
from src.data.preprocess import preprocess_movies
from src.features.vectorizer import build_similarity_matrix
from src.models.recommender import MovieRecommender


if __name__ == "__main__":
    df = load_raw_data()
    clean_df = preprocess_movies(df)

    similarity, _ = build_similarity_matrix(clean_df)

    recommender = MovieRecommender(clean_df, similarity)

    print(recommender.recommend("Spider-Man"))
