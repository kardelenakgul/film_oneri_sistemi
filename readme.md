# Akıllı Film Öneri Platformu (Movie Recommendation System)

Bu proje; film özetleri, türleri, yönetmenleri ve oyuncu kadrosu gibi metinsel öznitelikleri vektörleştirerek **Kosinüs Benzerliği (Cosine Similarity)** algoritması üzerinden benzer içerikleri bulan ve **Streamlit** ile sunulan **uçtan uca bir İçerik Tabanlı Öneri Sistemi (Content-Based Recommendation Engine)** uygulamasıdır.

---

## 🌟 Öne Çıkan Özellikler

- **🧠 İçerik Havuzu (Metadata Soup):** Film türü, yönetmen, başrol oyuncuları ve özet bilgilerini tek bir zengin öznitelik havuzunda birleştirir.
- **📐 Kosinüs Benzerliği Matrisi (Cosine Similarity):** Filmleri sayısal vektör uzayına taşıyarak aralarındaki açısal benzerlik skorlarını ($N \times N$ matrisi) hesaplar.
- **⚡ Hızlı Tahminleme (.pkl):** Hesaplanan benzerlik matrisini dondurarak web arayüzünde milisaniyeler içinde anlık öneri üretir.
- **📊 İnteraktif Arayüz (Streamlit):** Kullanıcının seçtiği filme en yakın 3 filmi benzerlik yüzdesi, tür, yönetmen, oyuncular ve Türkçe özet kartlarıyla listeler.

---

## Kullanılan Teknolojiler

- **Dil:** Python 3.13
- **Veri Manipülasyonu:** Pandas, NumPy
- **Matematik & Makine Öğrenmesi:** Scikit-Learn (`CountVectorizer`, `cosine_similarity`)
- **Web Arayüzü:** Streamlit
- **Model / Matris Serileştirme:** Joblib, Pickle

---

## 📁 Proje Klasör Yapısı

```text
film_oneri_sistemi/
│
├── dataset_downloader.py   # Film veri setini oluşturan modül
├── recommender_engine.py   # Benzerlik matrisini hesaplayan ve donduran motor
├── app.py                  # Streamlit web arayüzü
│
├── movies.csv              # Ham veri seti
├── movies_list.pkl         # İşlenmiş film listesi
├── similarity_matrix.pkl   # Eğitilmiş Kosinüs Benzerlik Matrisi
└── README.md               # Proje dokümantasyonu