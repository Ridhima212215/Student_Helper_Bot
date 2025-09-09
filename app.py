
from openai import OpenAI
import streamlit as st

import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
        page_bg = f"""
    <style>
    .block-container {{
        padding-top: 2rem; /* Reduces the top padding */
    }}

    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;   /* Correctly scales the image */
        background-repeat: no-repeat; /* Avoid tiling */
        background-attachment: fixed; /* Keeps it fixed on scroll */
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)


add_bg_from_local("assets/b4.jpg")


# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # fast + cheap model
        messages=[
            {"role": "system", "content": "You are an expert in summarizing text concisely and briefly for a student."},
            {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content


# Initialize Streamlit app
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

#
if "user_input" not in st.session_state:
    st.session_state.user_input_text = ""

# Define the chatbot function


def student_bot(question):
    # global st.session_state.conversation_history
    messages = []
    for q, a in st.session_state.conversation_history:
        messages.append({"role": "user", "content": q})
        messages.append({"role": "assistant", "content": a})

    # Add the new question
    messages.append({"role": "user", "content": question})

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # fast + cheap model
        messages=messages
    )
    answer = response.choices[0].message.content
    st.session_state.conversation_history.append((question, answer))
    st.session_state.conversation_history = st.session_state.conversation_history[-5:]
    return answer


st.title(" 👩🏻‍🎓Student Helper Chatbot")


# Form for user input
with st.form(key="chat_form", clear_on_submit=False):
    user_input = st.text_input(
        "Ask me anything:",
        value=st.session_state.user_input_text,
        key="user_input_box")
    submitted = st.form_submit_button("Send")

    if submitted and user_input:
        with st.spinner("Thinking..."):
            answer = student_bot(user_input)
            # st.session_state.user_input_text = ""


# for displaying full ans:
for i, (q, a) in enumerate(st.session_state.conversation_history):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f"**You:**")
    with col2:
        st.markdown(f"{q}")

    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f"**Bot:**")
    with col2:
        st.markdown(f"{a}")

        if st.button("Summarize", key=f"summarize_{i}"):
            with st.spinner("Summarizing..."):
                summary = summarize_text(a)
                st.info(f"**Summary:** {summary}")


# on click of clear button
if (st.button("Clear Chat")):
    st.session_state.conversation_history = []
    st.session_state.user_input_text = ""
    st.rerun()
