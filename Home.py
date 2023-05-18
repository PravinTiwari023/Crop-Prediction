import streamlit as st
import pickle
import helpSqllite as help
import pandas as pd
from datetime import datetime
import io


with open('dataset1.pkl', 'rb') as file:
    crop = pickle.load(file)

st.sidebar.success("Select a demo above.")

help.sidebardesign()

st.title(":blue[Crop Selection According To Environment Using Latest Technique Of Machine Learning]")

st.header("Dataset:")
st.write(crop)
with st.expander("See explanation"):
    st.markdown("""
    Precision agriculture is in trend nowadays. It helps the farmers to get informed decision about the farming strategy. Here, I present you a dataset which would allow the users to build a predictive model to recommend the most suitable crops to grow in a particular farm based on various parameters.

    => Context
    
    This dataset was build by augmenting datasets of rainfall, climate and fertilizer data available for India.
    
    => Data fields
    * N - ratio of Nitrogen content in soil
    * P - ratio of Phosphorous content in soil
    * K - ratio of Potassium content in soil
    * temperature - temperature in degree Celsius
    * humidity - relative humidity in %
    * ph - ph value of the soil
    * rainfall - rainfall in mm
    """)
st.header("Data information")
buffer = io.StringIO()
crop.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

st.header("Data Mathematical Information")
st.write(crop.describe())

col1, col2= st.columns(2)

with col1:
    st.header("Crop Types")
    types = crop.label.unique()
    label = pd.DataFrame(types,columns=["Crops"])
    st.write(label)

with col2:
    st.header("Crop Count")
    new_data = crop['label'].value_counts()
    st.write(new_data)


st.write(datetime.today())

