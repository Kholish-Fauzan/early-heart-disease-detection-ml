import streamlit as st
import pickle
import numpy as np

# Load model
with open('Best_Model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set page configuration
st.set_page_config(page_title="Heart Disease Predictor", page_icon="💓", layout="centered")

# Title & Description
st.title("💓 Heart Disease Prediction")
st.markdown(
    "Masukkan informasi medis berikut untuk memprediksi kemungkinan adanya penyakit jantung. "
    "Model ini dibangun berdasarkan data kesehatan pasien."
)

with st.expander("ℹ️ Penjelasan Singkat Fitur Input"):
    st.markdown("""
    - **Age**: Usia pasien (tahun)  
    - **Sex**: Jenis kelamin (Male/Female)  
    - **Chest Pain Type**: Jenis nyeri dada:  
        - TA: Typical Angina  
        - ATA: Atypical Angina  
        - NAP: Non-Anginal Pain  
        - ASY: Asymptomatic  
    - **RestingBP**: Tekanan darah saat istirahat (mmHg)  
    - **Cholesterol**: Kolesterol total (mg/dL)  
    - **FastingBS**: Apakah gula darah puasa > 120 mg/dL?  
    - **RestingECG**: Hasil EKG saat istirahat  
    - **MaxHR**: Denyut jantung maksimum  
    - **ExerciseAngina**: Apakah mengalami angina saat olahraga?  
    - **Oldpeak**: Depresi ST akibat olahraga relatif terhadap saat istirahat  
    - **ST_Slope**: Kemiringan segmen ST: Up, Flat, Down  
    """)

st.markdown("---")

# Form input
with st.form("heart_form"):
    st.subheader("📝 Data Pasien")
    
    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Usia", 20, 100, 50)
        sex = st.radio("Jenis Kelamin", ["Pria", "Wanita"])
        resting_bp = st.number_input("Tekanan Darah Saat Istirahat (mmHg)", 80, 200, 120)
        cholesterol = st.number_input("Kolesterol Total (mg/dL)", 100, 600, 200)
        max_hr = st.slider("Denyut Jantung Maksimum", 60, 220, 150)

    with col2:
        chest_pain = st.selectbox("Tipe Nyeri Dada", ["TA", "ATA", "NAP", "ASY"])
        fasting_bs = st.radio("Gula Darah Puasa > 120 mg/dL?", ["Ya", "Tidak"])
        resting_ecg = st.selectbox("Hasil EKG Saat Istirahat", ["Normal", "ST", "LVH"])
        exercise_angina = st.radio("Angina Saat Olahraga?", ["Ya", "Tidak"])
        oldpeak = st.slider("Oldpeak (depresi ST)", -2.0, 6.5, 1.0, 0.1)
        st_slope = st.selectbox("Kemiringan ST Slope", ["Up", "Flat", "Down"])

    submitted = st.form_submit_button("🔍 Prediksi Sekarang")

# Jika tombol diklik
if submitted:
    # Encode input sesuai model
    sex = 1 if sex == "Pria" else 0
    fasting_bs = 1 if fasting_bs == "Ya" else 0
    exercise_angina = 1 if exercise_angina == "Ya" else 0

    chest_pain_encoded = [0, 0, 0]
    if chest_pain == "ATA": chest_pain_encoded[0] = 1
    elif chest_pain == "NAP": chest_pain_encoded[1] = 1
    elif chest_pain == "TA": chest_pain_encoded[2] = 1

    resting_ecg_encoded = [0, 0]
    if resting_ecg == "ST": resting_ecg_encoded[0] = 1
    elif resting_ecg == "LVH": resting_ecg_encoded[1] = 1

    st_slope_encoded = [0, 0]
    if st_slope == "Flat": st_slope_encoded[0] = 1
    elif st_slope == "Up": st_slope_encoded[1] = 1

    # Gabungkan ke array
    input_data = np.array([[
        age, sex, resting_bp, cholesterol, fasting_bs, max_hr,
        exercise_angina, oldpeak,
        *chest_pain_encoded,
        *resting_ecg_encoded,
        *st_slope_encoded
    ]])

    # Prediksi
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]

    # Tampilkan hasil
    st.markdown("---")
    if prediction == 1:
        st.error(f"⚠️ Hasil Prediksi: **Kemungkinan Terkena Penyakit Jantung**\n\nProbabilitas: **{proba:.2%}**")
    else:
        st.success(f"✅ Hasil Prediksi: **Tidak Terindikasi Penyakit Jantung**\n\nProbabilitas: **{proba:.2%}**")
