import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
st.title("Data ")

st.header("Upload data file")
data_file = st.file_uploader('Choose a csv file', type=(['.csv']))

if data_file is not None:
  df = pd.read_csv(data_file)
  st.header("Show data")
  st.dataframe(df)
  st.header('Descriptive statistics')
  st.table(df.describe())
  st.header('Show data information')
  buffer = io.StringIO()
  st.write(buf=buffer)
  st.text(buffer.getvalue())
  st.header("Visualize each atrribute")
  for col in list(df.columns):
    fig, ax = plt.subplots()
    ax.hist(df[col], bins=20)
    plt.xlabel(col)
    plt.ylabel('Quanity')
    st.pyplot(fig)
