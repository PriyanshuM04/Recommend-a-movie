from src.data.load_data import load_raw_data
from src.data.preprocess import preprocess_movies


if __name__ == "__main__":
    df = load_raw_data()
    clean_df = preprocess_movies(df)

    print(clean_df.shape)
    print(clean_df.head())
