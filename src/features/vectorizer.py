from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def build_similarity_matrix(
    df: pd.DataFrame,
    max_features: int = 5000
):
    """
    Builds cosine similarity matrix from movie tags.
    
    Returns:
        similarity_matrix (ndarray)
        vectorizer (CountVectorizer)
    """
    cv = CountVectorizer(
        max_features=max_features,
        stop_words="english"
    )

    vectors = cv.fit_transform(df["tags"]).toarray()
    similarity = cosine_similarity(vectors)

    return similarity, cv
