import os

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Data directories
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")

# CSV file paths
MOVIES_CSV = os.path.join(RAW_DATA_DIR, "movies.csv")
CREDITS_CSV = os.path.join(RAW_DATA_DIR, "credits.csv")
