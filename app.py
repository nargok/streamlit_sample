import streamlit as st
import pandas as pd
import numpy as np

st.title("Sample App")

if st.button("Click Me"):
    st.write("Clicked")

# options = st.multiselect(
#     'What are you favorite colors?',
#     ['Green', 'Yellow', 'Red', 'Blue'],
#     ['Red']
# )

# st.write(f'選択肢: {options}')

number = st.sidebar.slider('pick a number', 0, 100)
st.sidebar.write(f'number: {number}')

left_col, right_col = st.columns(2)

options = left_col.multiselect(
    'What are you favorite colors?',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Red']
)

right_col.write(f'選択肢: {options}')