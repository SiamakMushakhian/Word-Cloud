import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image
from wordcloud import STOPWORDS, ImageColorGenerator, WordCloud

st.write("""# What is Word Cloud?
It is a beautiful isualization format to highlight important textual data points.
""")

cols = st.columns(3)
cols[1].image(Image.open('wordcloud.png'), width=250)

def load_image(image_file):
	img = Image.open(image_file)
	return img

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
if image_file is not None:
    # To View Uploaded Image
    st.image(load_image(image_file), width=250)
