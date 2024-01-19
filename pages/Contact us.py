import streamlit as st
import helpSqllite as help

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.sidebar.header("Plotting Demo")

help.sidebardesign()

import streamlit as st

def contact_us():
    st.title(":blue[Contact Us]")

    st.write("Please fill out the form below to get in touch with us.")

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message", height=150)

    if st.button("Submit"):
        # Add your logic to handle the submission of the form here
        # For example, you can send an email with the submitted details or save them to a database
        # You can also display a success message to the user

        st.success("Thank you for reaching out! We will get back to you soon.")

if __name__ == "__main__":
    contact_us()
