import streamlit as st
import helpSqllite as help

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

help.sidebardesign()

st.sidebar.header("Plotting Demo")

st.header(":blue[About]")

st.write("""
Welcome to Crop Prediction ML! We are a team of highly motivated final year students from Lovely Professional University, specializing in Machine Learning and Deep Learning. Our passion for this field drives us to develop cutting-edge solutions for agricultural forecasting and crop prediction.

At Crop Prediction ML, we believe that harnessing the power of artificial intelligence can revolutionize the way we approach agriculture. By leveraging the potential of Machine Learning and Deep Learning algorithms, we aim to provide accurate and timely predictions regarding crop yields, disease outbreaks, and optimal farming practices.

Our journey began during our time at Lovely Professional University, where we received comprehensive training in various aspects of data science and artificial intelligence. This robust academic foundation, coupled with our unwavering dedication, has equipped us with the knowledge and skills necessary to tackle complex challenges in the agricultural sector.

With a deep understanding of the potential impact of Machine Learning and Deep Learning in agriculture, we are committed to bridging the gap between technology and the farming community. Our primary objective is to empower farmers with actionable insights that can enhance their decision-making process, optimize resource allocation, and increase crop productivity.

At Crop Prediction ML, we follow a rigorous approach to develop our models. We gather vast amounts of historical and real-time agricultural data, including weather patterns, soil composition, crop varieties, and farming techniques. By employing advanced algorithms and leveraging the power of deep neural networks, we train our models to analyze these datasets and generate accurate predictions for various crop-related parameters.

We understand that the success of our predictions relies on the quality and relevance of the data we use. Therefore, we continuously strive to improve our data collection methods, ensuring that our models are trained on the most up-to-date and reliable information available.

Our commitment to excellence extends beyond the development of robust machine learning models. We value transparency and believe in fostering strong relationships with our users. We actively seek feedback from farmers, agronomists, and industry experts, incorporating their insights into our models to enhance their effectiveness and relevance.

At Crop Prediction ML, we envision a future where technology and agriculture seamlessly intertwine to create sustainable farming practices, maximize crop yields, and ensure food security. We are driven by our passion for Machine Learning and Deep Learning, and we are excited to make a meaningful impact in the agricultural sector.

Join us on this transformative journey as we pave the way for a smarter, more efficient, and sustainable future for agriculture. Together, we can revolutionize crop prediction and contribute to a world where farming thrives with the power of artificial intelligence.""")