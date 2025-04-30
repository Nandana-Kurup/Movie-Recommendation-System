import streamlit as st
import base64

st.set_page_config(page_title="Movie Recommender", layout="wide")

# Background image
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
        }}
        .centered {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: rgba(0, 0, 0, 0.6);
            padding: 40px 60px;
            border-radius: 15px;
            color: white;
            text-align: center;
        }}
        h1 {{
            font-size: 3em;
            color: #00bcd4;
        }}
        </style>
        <div class="centered">
            <h1> </h1>
            <h1>Welcome to Movie Recommender 🎬</h1>
            <br>
            <p>Click on app to see Recommendation page & Chatbot </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Setting backgorund image
set_background("3.jpg")
