import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil_model.sav', 'rb'))

st.title('Estimasi Harga Mobil')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Jarak Tempuh Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Ukuran Mesin Mobil')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write('Estimasi Harga Mobil = ', predict)
    st.write('Estimasi Harga Mobil Dalam IDR = ', predict*19000)