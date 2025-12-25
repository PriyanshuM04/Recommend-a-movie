# Movie Recommendation System

A **content-based movie recommender system** built with Python and Flask that suggests movies similar to a user-provided title. The app integrates with **TMDB API** to fetch movie posters dynamically and provides an interactive web interface for exploring recommendations.

---

## Features

- Content-based movie recommendation using **precomputed similarity matrices**.
- Web interface built with **Flask** for interactive user experience.
- Fetches movie posters dynamically using **TMDB API**.
- Handles large datasets efficiently using **pandas** and **scikit-learn**.
- Provides smooth and responsive display of recommendations.

---

## Technologies Used

- Python 3.13  
- Flask  
- pandas, numpy, scikit-learn  
- TMDB API  
- pickle for saving/loading precomputed data  

---

## Project Structure

```

├── app/
│   ├── **init**.py         # Flask app creation
│   ├── routes.py           # Application routes and recommendation logic
│   └── templates/          # HTML templates
├── models/
│   ├── clean_df.pkl        # Preprocessed movie dataset
│   └── similarity.pkl      # Precomputed similarity matrix
├── requirements.txt
├── wsgi.py
└── README.md

````

---

## Setup & Installation

1. **Clone the repository**
```bash
git clone https://github.com/PriyanshuM04/Recommend-a-movie.git
cd Recommend-a-movie
````

2. **Create a virtual environment and activate it**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

* Create a `.env` file in the project root:

```env
TMDB_API_KEY=your_tmdb_api_key
```

5. **Run the application**

```bash
python wsgi.py
```

* Visit `http://127.0.0.1:5000` in your browser.

---

## Usage

1. Enter the name of a movie in the search box.
2. Click **Submit**.
3. The system will display a list of recommended movies along with their posters.

---

## Notes

* The project uses precomputed data (`clean_df.pkl` and `similarity.pkl`) to speed up recommendations.
* `similarity.pkl` is a large file (~180 MB), so make sure it is included in the `models/` folder.

---

## Future Improvements

* Deploy the application on cloud platforms (e.g., Render, Heroku) with dynamic model loading.
* Add user-based collaborative filtering for personalized recommendations.
* Optimize poster fetching with caching for faster load times.

---

## Author

**Priyanshu Mallick** – B.Tech Electrical Engineering, BIT Sindri
[GitHub](https://github.com/PriyanshuM04)
