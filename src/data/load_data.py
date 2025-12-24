import pandas as pd
from src.config.config import MOVIES_CSV, CREDITS_CSV

def load_raw_data():
    """
    Docstring for load_raw_data
    """
    movies = pd.read_csv(MOVIES_CSV)
    credits = pd.read_csv(CREDITS_CSV)

    df = movies.merge(credits, on="title")
    return df