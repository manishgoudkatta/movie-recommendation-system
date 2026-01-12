import streamlit as st
import pickle
import pandas as pd

# -------------------
# Load Data
# -------------------

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


# -------------------
# Recommendation Function
# -------------------

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:13]  # Top 12

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# -------------------
# Streamlit UI
# -------------------

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

st.title("🎬 Movie Recommender System")
st.write("Select a movie and get top 12 recommendations in a neat card layout!")

selected_movie = st.selectbox(
    "Select a movie:",
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)

    st.subheader("Top Recommendations:")

    # Display cards in 4 columns per row
    num_cols = 4
    cols = st.columns(num_cols)

    for i, movie_name in enumerate(recommendations):
        with cols[i % num_cols]:
            st.markdown(
                f"""
                <div style="
                    padding:20px; 
                    border-radius:15px; 
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    color:white;
                    text-align:center;
                    font-weight:bold;
                    font-size:18px;
                    box-shadow: 2px 4px 12px rgba(0,0,0,0.2);
                    margin-bottom:10px;
                ">
                    {movie_name}
                </div>
                """,
                unsafe_allow_html=True
            )
