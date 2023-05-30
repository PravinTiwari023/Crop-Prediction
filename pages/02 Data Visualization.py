import streamlit as st
import pickle
import helpSqllite
from PIL import Image

with open('dataset1.pkl', 'rb') as file:
    crop = pickle.load(file)

st.set_page_config(page_title="Plotting Graphs", page_icon="📈")

helpSqllite.hide_watermark()
helpSqllite.sidebardesign()

st.sidebar.header("Visualization")

st.title(":blue[Visualizations]")

new_data1 = crop[["N","P","K"]]
new_data2 = crop[["humidity","temperature"]]
new_data3 = crop[["ph","rainfall"]]

tab1, tab2, tab3 = st.tabs(["N vs P vs K", "Temperature vs Humidity", "ph vs Rainfall"])

with tab1:
    st.line_chart(new_data1)

with tab2:
    st.line_chart(new_data2)

with tab3:
    st.line_chart(new_data3)

image1 = Image.open("Screenshot (59).png")
image2 = Image.open("Screenshot (60).png")
image3 = Image.open("Screenshot (61).png")
image4 = Image.open("Screenshot (62).png")
image5 = Image.open("Screenshot (63).png")

st.image(image1,"distribution 1")
st.image(image2,"distribution 2")
st.image(image3,"distribution 3")
st.image(image4,"Temperature vs Label")
st.image(image5,"Temperature vs ph")