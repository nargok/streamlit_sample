import streamlit as st
import pandas as pd
import numpy as np

st.title("Sample App")

st.write(np.random.randn(20, 3),)

df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']  
)

# line_chart
# st.line_chart(df)

# area_chart
# st.area_chart(df)

# bar_chart
st.bar_chart(df)