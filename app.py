import os
import pickle
import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY") or os.getenv("api_key")

if not TMDB_API_KEY:
    st.error("TMDB_API_KEY not found. Add it to your .env file as TMDB_API_KEY=<your_key>.")


def fetch_poster(movie_id):
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, TMDB_API_KEY)
        data = requests.get(url, timeout=300)
        data = data.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except Exception as e:
        print(f"Error fetching poster for movie_id {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Error"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    top_20 = distances[1:21]

    candidates = []
    for i, score in top_20:
        movie_id = movies.iloc[i]['movie_id']
        dt_row = dt_features[dt_features['movie_id'] == movie_id]

        if not dt_row.empty:
            features = dt_row[['popularity', 'runtime', 'vote_count']].values
            quality = dt.predict(features)[0]
        else:
            quality = 0

        candidates.append((i, score, quality))

    candidates.sort(key=lambda x: (-x[2], -x[1]))

    recommended_movie_names = []
    recommended_movie_posters = []
    for idx, _, _ in candidates[:5]:
        movie_id = movies.iloc[idx].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[idx].title)

    return recommended_movie_names, recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
dt = pickle.load(open('dt_model.pkl', 'rb'))
dt_features = pickle.load(open('dt_features.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
