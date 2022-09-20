import streamlit as st

st.title("Jorge, You are Dead!!!!")

my_text = st.text("Press The RUN Command!")
my_button = st.button("RUN Command")

if my_button:
    st.title("We are executing your Death!")
    my_text = st.text("You are and Angel now!")

my_text = st.text("Now, kill another one!!")

