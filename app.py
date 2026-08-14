import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

st.set_page_config(
    page_title="Akıllı Film Keşif Platformu", page_icon="🎬", layout="wide"
)

st.title("🎬 Akıllı Film Öneri Platformu")
st.caption(
    "Kosinüs Benzerliği (Cosine Similarity) ve Doğal Dil İşleme (NLP) tabanlı film tavsiye motoru."
)


def load_data():
    movies_df = pd.read_pickle("movies_list.pkl")
    similarity = joblib.load("similarity_matrix.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    feature_mat = joblib.load("feature_matrix.pkl")
    return movies_df, similarity, vectorizer, feature_mat


movies, similarity_matrix, cv, feature_matrix = load_data()


# 1. Filme Göre Öneri
def get_recommendations_by_movie(movie_title, top_n=3):
    movie_idx = movies[movies["title"] == movie_title].index[0]
    similarity_scores = list(enumerate(similarity_matrix[movie_idx]))
    sorted_movies = sorted(
        similarity_scores, key=lambda x: x[1], reverse=True
    )[1 : top_n + 1]

    results = []
    for idx, score in sorted_movies:
        row = movies.iloc[idx]
        results.append(
            {
                "title": row["title"],
                "genres": row["genres"],
                "director": row["director"],
                "cast": row["cast"],
                "overview": row["overview"],
                "similarity_score": round(score * 100, 1),
            }
        )
    return results


# 2. Serbest Arama / Prompt
def get_recommendations_by_text(user_query, top_n=3):
    query_vector = cv.transform([user_query])
    similarity_scores = cosine_similarity(query_vector, feature_matrix).flatten()
    sorted_indices = similarity_scores.argsort()[::-1][:top_n]

    results = []
    for idx in sorted_indices:
        row = movies.iloc[idx]
        results.append(
            {
                "title": row["title"],
                "genres": row["genres"],
                "director": row["director"],
                "cast": row["cast"],
                "overview": row["overview"],
                "similarity_score": round(similarity_scores[idx] * 100, 1),
            }
        )
    return results


tab1, tab2 = st.tabs(
    ["🎯 Filme Göre Öneri", "🔍 Konu / Cümle Yazarak Film Bul"]
)

with tab1:
    col1, col2 = st.columns([3, 1])
    with col1:
        selected_movie = st.selectbox(
            "İzlediğiniz / Beğendiğiniz Bir Film Seçin:",
            movies["title"].values,
        )
    with col2:
        st.write("")
        st.write("")
        btn_movie = st.button(
            "🍿 Benzerlerini Öner", type="primary", use_container_width=True
        )

    if btn_movie:
        results = get_recommendations_by_movie(selected_movie)
        st.subheader(f"✨ '{selected_movie}' Sevenler İçin Önerilen Filmler:")
        cols = st.columns(3)
        for i, m in enumerate(results):
            with cols[i]:
                st.markdown(f"### 🎥 {m['title']}")
                st.caption(f"🔥 Benzerlik: %{m['similarity_score']}")
                st.write(f"🎭 **Tür:** `{m['genres']}`")
                st.write(f"🎬 **Yönetmen:** {m['director']}")
                st.info(f"📝 **Özet:** {m['overview']}")

with tab2:
    user_prompt = st.text_input(
        "Nasıl bir film arıyorsunuz? (Örn: 'uzayda geçen macera', 'süper kahraman aksiyon', 'büyü okul')",
        "",
    )
    btn_text = st.button("Filmleri Keşfet 🚀")

    if btn_text and user_prompt:
        results = get_recommendations_by_text(user_prompt)
        st.subheader(f"'{user_prompt}' İçin En Uygun Filmler:")
        cols = st.columns(3)
        for i, m in enumerate(results):
            with cols[i]:
                st.markdown(f"### 🎥 {m['title']}")
                st.caption(f"🎯 Uyumluluk: %{m['similarity_score']}")
                st.write(f"🎭 **Tür:** `{m['genres']}`")
                st.write(f"🎬 **Yönetmen:** {m['director']}")
                st.info(f"📝 **Özet:** {m['overview']}")