import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image
from wordcloud import STOPWORDS, ImageColorGenerator, WordCloud

st.write("""# What is Word Cloud?
It is a beautiful visualization format to highlight important textual data points based on the word frequency.
""")

def load_image(image_file):
	img = Image.open(image_file)
	return img

cols = st.columns(3)
cols[1].image(load_image('wordcloud.png'), width=250)

st.write("""For this type of visualiztion, you need two files:
## 1) Document
Which consist the words  """)
docx_file = st.file_uploader("Upload Document", type=["pdf","docx","txt"])

st.write("""## 2) Image
It is the desired picture where you want to find your visuzlization on  """)
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
if image_file is not None:
    st.image(load_image(image_file), width=250)

st.write("""##  Customization
Choose the below option as like to find your word cloud""")

cols = st.columns(2)
back_color =cols[0].text_input("What color do you want as the background color of your word cloud?")

stopwords_choice = cols[1].radio("Do you want to use stopwords option?", options=['Yes', 'No'])
if stopwords_choice == 'Yes':
    stopwords = set(STOPWORDS)
else:
    stopwords = None

if docx_file is not None:
    raw_text = str(docx_file.read(),"utf-8")
    st.text(raw_text)

if image_file is not None:
    custom_mask = np.array(load_image(image_file))

# wc = WordCloud(background_color = 'white', 
#             stopwords = stopwords, 
#             mask = custom_mask, 
#             colormap='gist_rainbow',
#             collocations=False, 
# #                contour_width = 3, 
# #                contour_color = 'black',
# #                max_font_size = 50, 
# #                max_words = 5, 
# #                height = 1000, 
# #                width = 1000
#             )

# st.write("To see your word cloud press visualization button")
# if st.button("Visualization"):
    
#     wc.generate(text)

#     image_colors = ImageColorGenerator(custom_mask)
#     wc.recolor(color_func = image_colors)

#     plt.rcParams['figure.figsize'] = [8.0, 8.0]
#     plt.rcParams['figure.dpi'] = 140
#     plt.imshow(wc, interpolation = 'bilinear')
#     plt.axis('off')
#     plt.show()


# wc.to_file('Spruce_cloud.png')