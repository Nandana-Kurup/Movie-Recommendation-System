import streamlit as st
import pickle
import pandas as pd
import numpy
import base64
import random

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict=pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie recommendation System')

selected_movie_name  = st.selectbox(
'What do you like to Watch?',
movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
        
# Sidebar menu
page = st.sidebar.radio("Navigate", ["Home", "Chatbot"])

if page == "Home":
    st.title("🎬 Recommendation System")
    st.write("What do you feel like Watching")
    

elif page == "Chatbot":
    st.title("🤖 Chatbot Assistant")
    
    

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "new_message" not in st.session_state:
        st.session_state.new_message = False

    # Display messages
    for msg in st.session_state.messages:
        st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")

    # User input
    user_input = st.text_input("Ask me something:", key="input")

    if user_input and not st.session_state.new_message:
        st.session_state.messages.append({"role": "user", "content": user_input})

        if "recommend" in user_input.lower():
            bot_reply = random.choice([
                "How about a thriller? Try 'Inception'.",
                "I recommend 'The Matrix'! It's a classic.",
                "Check out 'The Dark Knight' if you love action!"
            ])
            
        elif "hello" in user_input.lower() or "hi" in user_input.lower():
            bot_reply = random.choice([
                "Hey! How can I help?",
                "Hello! 😊 What can I do for you?",
                "Hi there! What's up?"
            ])
            
        elif "movie" in user_input.lower():
            bot_reply = random.choice([
                "Need a good movie? I can help!",
                "Looking for a movie? Any genre in mind?",
                "Got a favorite genre? Let's find a movie."
            ])
            
        elif "thank" in user_input.lower():
            bot_reply = random.choice([
                "You're welcome! 😊",
                "No problem!",
                "Glad I could help!"
            ])
            
        elif "how are you" in user_input.lower():
            bot_reply = random.choice([
                "I'm great, thanks for asking! How about you?",
                "I'm doing well, thanks! What can I do for you?",
                "Doing awesome! How can I assist you?"
            ])
        elif "name" in user_input.lower():
            bot_reply = "I'm MovieBot, your movie guide!"
            
        else:
            bot_reply = random.choice([
                "I can help with movie suggestions.",
                "Let me know if you need a recommendation.",
                "What genre are you interested in?"
            ])
        

        st.session_state.messages.append({"role": "bot", "content": bot_reply})
        st.session_state.new_message = True
        st.rerun()

    if st.session_state.new_message:
        st.session_state.new_message = False
        
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_half_background(image_path):
    bin_str = get_base64_of_bin_file(image_path)
    css = f"""
    <style>
    .main-container {{
        display: flex;
        flex-direction: row;
        height: 100vh;
    }}

    .left-half {{
        flex: 1;
        background-image: url("D:\Movie\3.jpg;base64,{bin_str}");
        background-size: cover;
        background-position: center;
    }}

    .right-half {{
        flex: 1;
        padding: 2rem;
        background-color: white;
    }}

    h1 {{
        color: #00bcd4;
        text-align: center;
    }}

    .stMarkdown h4, .stMarkdown p {{
        color: #00bcd4;
    }}
    </style>

    <div class="main-container">
        <div class="left-half"></div>
        <div class="right-half">
    """
    st.markdown(css, unsafe_allow_html=True)
