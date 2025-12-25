from dotenv import load_dotenv
import os
import requests
import pickle
from flask import render_template, request, Blueprint
from src.models.recommender import MovieRecommender

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

bp = Blueprint("main", __name__)

# Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "..", "models")
os.makedirs(MODELS_DIR, exist_ok=True)

# File paths
CLEAN_DF_PATH = os.path.join(MODELS_DIR, "clean_df.pkl")
SIMILARITY_PATH = os.path.join(MODELS_DIR, "similarity.pkl")

# Optional: ENV var for similarity download URL
SIMILARITY_URL = os.getenv("SIMILARITY_URL")  # e.g., Google Drive direct link

# Download similarity.pkl if missing
if not os.path.exists(SIMILARITY_PATH):
    print("Downloading similarity.pkl...")
    if not SIMILARITY_URL:
        raise RuntimeError("SIMILARITY_URL not set in environment variables")
    r = requests.get(SIMILARITY_URL, stream=True)
    r.raise_for_status()
    with open(SIMILARITY_PATH, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Downloaded similarity.pkl successfully!")

# Load pickled artifacts
with open(CLEAN_DF_PATH, "rb") as f:
    clean_df = pickle.load(f)

with open(SIMILARITY_PATH, "rb") as f:
    similarity = pickle.load(f)

recommender = MovieRecommender(clean_df, similarity)

# Fetch posters from TMDB
def fetch_poster(movie_title):
    try:
        url = (
            "https://api.themoviedb.org/3/search/movie"
            f"?api_key={TMDB_API_KEY}&query={movie_title}"
        )
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        results = data.get("results")
        if results:
            poster_path = results[0].get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except Exception as e:
        print(f"TMDB error for '{movie_title}':", e)
    return None

@bp.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    posters = []

    if request.method == "POST":
        movie_title = request.form.get("movie")
        try:
            recommendations = recommender.recommend(movie_title)
            posters = [fetch_poster(m) for m in recommendations]
        except ValueError:
            recommendations = ["Movie not found"]
            posters = [None]

    movie_data = list(zip(recommendations, posters))
    return render_template("index.html", recommendations=movie_data)
