import pandas as pd
import numpy as np


class MovieRecommender:
    def __init__(self, movies_df: pd.DataFrame, similarity_matrix: np.ndarray):
        self.movies_df = movies_df.reset_index(drop=True)
        self.similarity = similarity_matrix

    def recommend(self, movie_title: str, top_n: int = 5):
        """
        Returns top N similar movies for a given movie title.
        """
        if movie_title not in self.movies_df["title"].values:
            raise ValueError(f"Movie '{movie_title}' not found in dataset.")

        index = self.movies_df[self.movies_df["title"] == movie_title].index[0]

        distances = list(enumerate(self.similarity[index]))
        distances = sorted(distances, key=lambda x: x[1], reverse=True)

        return [
            self.movies_df.loc[i[0], "title"]
            for i in distances[1 : top_n + 1]
        ]
