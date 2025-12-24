import ast
import pandas as pd
from nltk.stem import PorterStemmer


ps = PorterStemmer()


def _convert(text):
    """Extract 'name' values from list of dicts stored as string."""
    return [i["name"] for i in ast.literal_eval(text)]


def _convert_cast(text):
    """Extract top 3 cast members."""
    cast = []
    for i, item in enumerate(ast.literal_eval(text)):
        if i < 3:
            cast.append(item["name"])
        else:
            break
    return cast


def _fetch_director(text):
    """Extract director name from crew."""
    for i in ast.literal_eval(text):
        if i["job"] == "Director":
            return [i["name"]]
    return []


def _remove_spaces(items):
    """Remove spaces in multi-word names."""
    return [i.replace(" ", "") for i in items]


def _stem_text(text):
    """Apply stemming to text."""
    return " ".join(ps.stem(word) for word in text.split())


def preprocess_movies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and preprocesses the raw movie dataset.
    Returns:
        pd.DataFrame with columns: movie_id, title, tags
    """
    df = df[
        ["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]
    ].dropna()

    df["genres"] = df["genres"].apply(_convert)
    df["keywords"] = df["keywords"].apply(_convert)
    df["cast"] = df["cast"].apply(_convert_cast)
    df["crew"] = df["crew"].apply(_fetch_director)

    df["overview"] = df["overview"].apply(lambda x: x.split())

    for col in ["genres", "keywords", "cast", "crew"]:
        df[col] = df[col].apply(_remove_spaces)

    df["tags"] = (
        df["overview"]
        + df["genres"]
        + df["keywords"]
        + df["cast"]
        + df["crew"]
    )

    df = df[["movie_id", "title", "tags"]]
    df["tags"] = df["tags"].apply(lambda x: " ".join(x)).apply(_stem_text)

    df = df[df["tags"].str.strip() != ""]

    return df
