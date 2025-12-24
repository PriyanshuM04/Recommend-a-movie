from src.data.load_data import load_raw_data
from src.data.preprocess import preprocess_movies
from src.features.vectorizer import build_similarity_matrix


if __name__ == "__main__":
    df = load_raw_data()
    clean_df = preprocess_movies(df)

    similarity, _ = build_similarity_matrix(clean_df)

    print(similarity.shape)
