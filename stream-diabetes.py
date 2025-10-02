import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav'))

#judul web
st.title('Data Mining Prediksi Diabetes')

Pregnancies = st.text_input ('input nilai Pregnancies')

Glucose = st.text_input ('input nilai Glucose')

BloodPressure = st.text_input ('input nilai Blood Pressure')

SkinThickness = st.text_input ('input nilai Skin Thickness')

Insulin = st.text_input ('input nilai Insulin')

BMI = st.text_input ('input nilai BMI')

DiabetesPredigreeFunction = st.text_input ('input nilai Diabetes Predigree Function')

Age = st.text_input ('input nilai Age')