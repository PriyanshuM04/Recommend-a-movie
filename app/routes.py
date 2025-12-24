from flask import render_template, request
from app import app
from src.models.recommender import MovieRecommender
import pickle

# Load pickled artifacts
with open("models/clean_df.pkl", "rb") as f:
    clean_df = pickle.load(f)

with open("models/similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

recommender = MovieRecommender(clean_df, similarity)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    if request.method == "POST":
        movie_title = request.form.get("movie")
        try:
            recommendations = recommender.recommend(movie_title)
        except ValueError:
            recommendations = ["Movie not found"]
    return render_template("index.html", recommendations=recommendations)
