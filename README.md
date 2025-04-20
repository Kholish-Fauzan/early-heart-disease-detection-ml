# 💓 Heart Disease Classification using Machine Learning

Proyek ini bertujuan untuk membangun model machine learning guna **memprediksi apakah seseorang berisiko terkena penyakit jantung** berdasarkan data klinis pasien seperti usia, tekanan darah, kadar kolesterol, dan lain-lain.

---

## 📊 Dataset

Dataset yang digunakan berasal dari Kaggle:  
[Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)

- Jumlah sampel: 918 baris  
- Label: `HeartDisease` (0 = tidak ada, 1 = ada penyakit jantung)

---

## 🔍 Tahapan Proyek

1. **Domain & Business Understanding**  
   - Fokus pada prediksi risiko penyakit jantung.
   - Model ini dapat digunakan sebagai alat bantu awal untuk deteksi risiko pasien.

2. **Data Understanding & Explorasi**  
   - Tidak ada missing value.
   - Ditemukan nilai yang tidak realistis (RestingBP & Cholesterol = 0).
   - Dilakukan encoding untuk fitur kategorikal.

3. **Data Preparation**  
   - Encoding: One-hot & label encoding
   - Normalisasi fitur numerik (jika diperlukan)
   - Split data: 80% training, 20% testing

4. **Modeling**  
   - Model yang diuji: Logistic Regression, Random Forest, KNN
   - Evaluasi menggunakan: Accuracy, Precision, Recall, F1-Score

5. **Hyperparameter Tuning**  
   - GridSearchCV digunakan untuk meningkatkan performa Random Forest.

6. **Evaluasi Akhir**  
   - Random Forest menghasilkan performa terbaik dengan akurasi ~85-86%

---

## 🧠 Hasil Model

| Model                 | Accuracy | Precision | Recall | F1-Score |
|-----------------------|----------|-----------|--------|----------|
| Logistic Regression   | 0.86     | 0.91      | 0.84   | 0.87     |
| Random Forest         | **0.85** | 0.88      | 0.85   | 0.87     |
| K-Nearest Neighbors   | 0.85     | 0.89      | 0.84   | 0.87     |
| **Random Forest (Tuned)** | **0.86**     | **0.89**      | **0.88**   | **0.88**     |

---

## 🌐 Deploy dengan Streamlit

Aplikasi prediksi juga dibuat dengan Streamlit agar pengguna dapat mencoba prediksi langsung.

🔗 [Link Aplikasi Streamlit](https://share.streamlit.io/username/heart-disease-classification)

---