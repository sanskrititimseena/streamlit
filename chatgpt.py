import pandas as pd
import streamlit as st
import numpy as np
import altair as alt

data = pd.read_csv("chatgpt1.csv")
print(data)

st.write(data)

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)


