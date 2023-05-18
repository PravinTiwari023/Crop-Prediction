import streamlit as st
import helpSqllite as help
import pickle
import crop_info as ci

with open('Randomforest.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

st.set_page_config(page_title="Crop Prediction", page_icon="📈")

st.sidebar.header("Crop prediction")

help.sidebardesign()

dict = {20:["Rice",ci.rice],11:["Maize",ci.maize],3:["Chickpea",ci.chickpea],9:["Kidneybeans",ci.Kidneybeans],18:["Pigeonpeas",ci.pigeonpeas],
        13:["Mothbeans",ci.Mothbeans],14:["Mungbean",ci.Mungbean],2:["Blackgram",ci.Blackgram],10:["lentil",ci.lentil],19:["pomegranate",ci.pomegranate],
        1:["banana",ci.banana],12:["Mango",ci.Mango],7:["grapes",ci.grapes],21:["Watermelon",ci.Watermelon],15:["Muskmelon",ci.Muskmelon],0:["Apple",ci.Apple],
        16:["Orange",ci.Orange],17:["Papaya",ci.Papaya],4:["Coconut",ci.Coconut],6:["Cotton",ci.Cotton],8:["Jute",ci.Jute],5:["Coffee",ci.Coffee]}


st.title(":blue[Crop Prediction]")

st.header("Enter the following information")

N = st.slider('Nitrogen :', 0, 145, 1)
P = st.slider('Potassium :', 5, 145, 1)
K = st.slider('Magnesium :', 5, 205, 1)
Temp = st.slider('Temperature :', 7.00, 45.00, 0.01)
humidity = st.slider('Humidity :', 10.00, 100.00, 0.1)
ph = st.slider('ph :', 0.0, 10.00, 0.01)
rain = st.slider('Rainfall :', 15.00, 300.00, 0.1)

feature_arr=[N,P,K,Temp,humidity,ph,rain]

clicked = st.button("Predict")

if clicked:
    prediction = loaded_model.predict([feature_arr])
    i = prediction[0]
    if i in dict.keys():
        st.success(dict[i][0])
        st.write("is the best crop under this circumstances")
        with st.expander("See Infomation"):
            st.write(dict[i][1])