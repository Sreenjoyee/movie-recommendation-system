# movie-recommendation-system
# 🎬 Movie Recommender System

A content-based movie recommendation system built using machine learning techniques. This project suggests similar movies based on user selection by analyzing features like genres, cast, keywords, and overview.

---

## 🚀 Features

* 🎯 Recommends top 5 similar movies
* 🧠 Uses content-based filtering
* 🖼️ Displays movie posters using TMDB API
* ⚡ Fast and interactive UI with Streamlit
* 🔍 Dropdown-based movie selection

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* Streamlit
* TMDB API

---

## 📊 How It Works

1. **Data Preprocessing**

   * Extracts important features like genres, cast, keywords, and overview
   * Cleans and transforms data into a usable format

2. **Feature Engineering**

   * Combines all relevant features into a single column called `tags`

3. **Text Vectorization**

   * Uses `CountVectorizer` to convert text into numerical vectors

4. **Similarity Calculation**

   * Computes cosine similarity between movies

5. **Recommendation**

   * Returns top 5 similar movies based on selected input

---

## 🖼️ API Used

* The Movie Database (TMDB) API
  Used to fetch movie posters dynamically.

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
```

---
## 📂 Dataset

This project does not include the dataset due to size limitations.

You can download the dataset from Kaggle:

👉 https://www.kaggle.com/tmdb/tmdb-movie-metadata

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🔑 API Key Setup

1. Create an account on TMDB
2. Generate an API key
3. Replace the API key in `app.py`:

```python
api_key = "YOUR_API_KEY"
```

---

## 📌 Future Improvements

* 🎨 Improve UI (Netflix-style layout)
* ⭐ Add movie ratings and overview display
* 🔍 Add search functionality
* 🌐 Deploy the app online

---

## 🙌 Acknowledgements

* TMDB for providing movie data
* Scikit-learn for machine learning tools
* Streamlit for UI framework

---

## 📜 License

This project is for educational purposes only.
