import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image
from wordcloud import STOPWORDS, ImageColorGenerator, WordCloud

st.write("""# What is Word Cloud?
It is a beautiful visualization format to highlight important textual data points based on the word frequency.
To generate your word cloud, you need two files, a text file and an image file, and set the parameters.
""")

def load_image(image_file):
	img = Image.open(image_file)
	return img

cols = st.columns(3)
cols[1].image(load_image('wordcloud.png'), width=300)

st.write("**1) Document**")
docx_file = st.file_uploader("Upload your text file here", type=["docx","txt"])
if docx_file is not None:
    text = str(docx_file.read(),"utf-8")


st.write("**2) Image**")
image_file = st.file_uploader("Upload your image file here", type=["png","jpg","jpeg"])
if image_file is not None:
    st.image(load_image(image_file), width=250)
    custom_mask = np.array(load_image(image_file))


st.write("**Parameters**")
cols = st.columns(2)
color_list = ['white', 'black', 'gray', 'red', 'blue', 'green', 'yellow', 'orange', 'brown', 'pink', 'purple']
background_color_choice =cols[0].selectbox("Background color:", color_list)

stopwords_choice = cols[1].radio("Do you want to use stopwords option?", options=['Yes', 'No'])
if stopwords_choice == 'Yes':
    stopwords = set(STOPWORDS)
else:
    stopwords = None

contour_choice = st.radio("Do you want to have a contour around your word cloud?", options=['Yes', 'No'], index=1)
cols = st.columns(2)
if contour_choice == 'Yes':
    contour_width_choice = cols[0].text_input("Choose the contour width")
    contour_color_choice = cols[1].selectbox("Choose the color of contour", color_list)

st.write("To see your word cloud press visualization button")
cols = st.columns(3)
if cols[1].button("Generator"):
    if docx_file is None:
        st.error("Please upload your text file.")
    elif image_file is None:
        st.error("Please upload your image file.")
    elif contour_width_choice == "":
        st.error("You need to specify the width of contour.")
    else:
        wc = WordCloud(mask = custom_mask,
                background_color = background_color_choice,
                stopwords = stopwords,
                contour_width=float(contour_width_choice),
                contour_color = contour_color_choice,
                colormap='gist_rainbow',
                collocations=False
    #                max_font_size = 50,
    #                max_words = 5
                )
        wc.generate(text)

        image_colors = ImageColorGenerator(custom_mask)
        wc.recolor(color_func = image_colors)

        # plt.rcParams['figure.figsize'] = [5.0, 5.0]
        # plt.rcParams['figure.dpi'] = 140
        plt.imshow(wc, interpolation = 'bilinear')
        # plt.axis('off')
        st.pyplot(plt)

        # st.write("If you want to download your word cloud, please choose the desired directory:")
        # cols = st.columns(3)
        # if cols[1].button("Download"):
        #     wc.to_file('Spruce_cloud.png')