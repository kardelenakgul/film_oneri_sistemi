import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_recommender_engine():
    print("📂 Veri seti okunuyor...")
    df = pd.read_csv("movies.csv")

    print("🧠 İçerik uzayı oluşturuluyor...")
    df["combined_features"] = (
        df["genres"]
        + " "
        + df["director"]
        + " "
        + df["cast"]
        + " "
        + df["overview"]
    )

    print("🔢 Vektör matrisi ve Kosinüs Benzerliği hesaplanıyor...")
    cv = CountVectorizer()
    feature_matrix = cv.fit_transform(df["combined_features"])
    similarity_matrix = cosine_similarity(feature_matrix)

    print("💾 Modeller kaydediliyor...")
    joblib.dump(cv, "vectorizer.pkl")
    joblib.dump(similarity_matrix, "similarity_matrix.pkl")
    joblib.dump(feature_matrix, "feature_matrix.pkl")
    df[["id", "title", "genres", "director", "cast", "overview"]].to_pickle(
        "movies_list.pkl"
    )

    print(f"🚀 TAMAMLANDI! {len(df)} film için tüm sistem hazır!")


if __name__ == "__main__":
    build_recommender_engine()