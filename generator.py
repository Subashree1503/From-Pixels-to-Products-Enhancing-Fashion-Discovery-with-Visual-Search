# Import libraries
import time
import timeit
import streamlit as st
from tensorflow.keras.preprocessing import image
image.LOAD_TRUNCATED_IMAGES = True
from io import BytesIO
import requests
from PIL import Image
from predictions import GenerateSimilarImages


# Function to add title
def add_title():
    st.markdown("""
    <style>
    .big-font {
        font-size:40px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="big-font : text-align: center">Fashion Image Search Engine</h1>', unsafe_allow_html=True)

# Function to open css file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Function to load the css file
def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

# Function to add the search icone
def icon(icon_name):
    st.sidebar.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

# Function to load teh query image
def load_input_url(input_url):
    response = requests.get(input_url)
    queryImage = Image.open(BytesIO(response.content))
    st.image(queryImage)

    return queryImage

# Function to add background image
def add_background():

    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/hand-painted-watercolor-abstract-background_23-2148998534.jpg?w=1380&t=st=1702021401~exp=1702022001~hmac=494a2b8e32b771e67850421786ca434f30fcd4d554d4bddef9f7ffef96b1d301");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

# Generate top 8 similar images
def return_similar_images(queryImage):

    # 1. Predictions Object
    sim_img_gen = GenerateSimilarImages(queryImage)

    # 2. generate output path
    _, top_8_images_path, top_8_images_desc, scores = sim_img_gen.generate_similar_images()

    # 3. Load these files
    print(st.image([top_8_images_path[i] for i in range(0, 4)], caption=['{} {}'.format(top_8_images_desc[i], scores[i]) for i in range(0,4)]))


    st.image([top_8_images_path[i] for i in range(0, 4)], caption=['{} {}'.format(top_8_images_desc[i], scores[i]) for i in range(0,4)])
    st.image([top_8_images_path[i] for i in range(4, 8)], caption=['{} {}'.format(top_8_images_desc[i], scores[i]) for i in range(4,8)])

# Main Function
if __name__ == '__main__':

    # 1. Add title
    add_title()

    # 2. Load the CCS file
    local_css("style.css")
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

    # 3. Add Background image
    add_background()

    # 4. Add a sidebar with text input and search icon
    add_selectbox = st.sidebar.text_input(
        "Women Fashion Image Search Engine",
        placeholder="Enter the Image URL"
    )
    icon('search')

    # 5. Create a Search Button
    button_clicked = st.sidebar.button("Search")

    # Execute the predictions
    # When the button is clicked
    if button_clicked:
        # Print the query image
        st.title('QUERY IMAGE')
        # Load the query image
        queryImage = load_input_url(add_selectbox)
        # Display the spinner
        with st.spinner('Wait for it...'):
            time.sleep(40)

        # Generate the results
        st.title("Images similar to your input...")
        # st.text_area("time taken to fetch images : ")
        start_time = time.time()
        return_similar_images(add_selectbox)
        end_time = time.time()
        elapsed_time = end_time - start_time
        st.text_area("time taken to fetch images : ", elapsed_time)