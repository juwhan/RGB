import streamlit as st
import pandas as pd


st.title("RGB value")


red = st.slider("Red", 0, 255)
red1 = hex(red)
if 17 > red:
    red1 = f"{red1}0"
st.write("16진수:", red1[2:4])


green = st.slider("Green", 0, 255)
green1 = hex(green)
if 17 > green:
    green1 = f"{green1}0"
st.write("16진수:", green1[2:4])


blue = st.slider("Blue", 0, 255)
blue1 = hex(blue)
if 17 > blue:
    blue1 = f"{blue1}0"
st.write("16진수:", blue1[2:4])


color = "{}{}{}".format(red1[2:4], green1[2:4], blue1[2:4])
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{background-color: #%s};
}
</style>
""" % color
st.subheader("RGB value is: #{}{}{}".format(
    red1[2:4], green1[2:4], blue1[2:4]))
st.markdown(page_bg_img, unsafe_allow_html=True)
