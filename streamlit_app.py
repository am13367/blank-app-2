import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns

st.title("🎈My new app")

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.sidebar.title("Select Database")

st.image("cat.jpeg")

app_mode = st.sidebar.selectbox('Select a page>>',["01 Introduction","02 Data Visualization"])

if app_mode == "01 Introduction":
    st.write ("Let's start exploring the dataset:")
    df = pd.read_csv("nn.csv")
    st.dataframe(df.head(5))
    st.markdown("###Statistics Summary of the dataset >> ")
    st.dataframe(df.describe())
    list og 

elif app_mode =="02 Data Visualization":
    st.write("Hello World")

    st.bar_chart.df(["name"])

