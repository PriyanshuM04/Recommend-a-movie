import pandas as pd
from src.config.config import MOVIES_CSV, CREDITS_CSV

def load_raw_data():
    """
    Loads and merges movies and credits datasets.
    Returns:
        pd.DataFrame
    """
    movies = pd.read_csv(MOVIES_CSV)
    credits = pd.read_csv(CREDITS_CSV)

    df = movies.merge(credits, on="title")
    return df