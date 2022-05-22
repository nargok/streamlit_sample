import streamlit as st
import pandas as pd
import numpy as np

st.title("Sample App")

if st.button("Click Me"):
    st.write("Clicked")

options = st.multiselect(
    'What are you favorite colors?',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Red']
)

st.write(f'選択肢: {options}')

number = st.slider('pick a number', 0, 100)
st.write(f'number: {number}')