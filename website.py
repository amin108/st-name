from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/e91327c2-8519-4712-9694-9f598529730e/DPyqHWkxUR.json")
img_lottie_animation = Image.open("images.jpeg")

with st.container():
    st.subheader("hi, i am amin :wave:")
    st.title("A Data analyst from iran")
    st.write("hello world i am developer from iran and my name is amin maghboul ")
    st.write("[learn more >>](https://pythonandvba.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what i do")
        st.write("##")
        st.write("if you wnat to know more about coding please come to my chanel")
        st.write("[my youtube chanel >>](https://youtube.com/c/CodingIsFun)")
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Project")
    st.write('##')
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("inegreat lottie animations inside Streamlit App")
        st.write("im amin maghboul and i want to be an developer and hacker in future")
        st.markdown("[watch Video...](https://youtu.be.TXSOitGoINE)")

with st.container():
    st.write('---')
    st.header("How put this site on internet for everyone")
    st.write('##')
    image_column, text_column = st.columns(2)
    with text_column:
        st.subheader("Put this website on internet")
        st.write("for more information click down link")
        st.markdown("[watch Video...](https://youtu.be.TXSOitGoINE)")
    