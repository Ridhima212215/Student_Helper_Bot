
from openai import OpenAI
import streamlit as st

import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
        page_bg = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: 100% 100%;   /* Stretches to fit width and height */
        background-repeat: no-repeat; /* Avoid tiling */
        background-attachment: fixed; /* Keeps it fixed on scroll */
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)


add_bg_from_local("C:\\Users\\Edimadakala\\Downloads\\b4.jpg")


# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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


# Test the bot
# print("🤖 Student Helper Chatbot")
# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["exit", "quit"]:
#         break
#     answer = student_bot(user_input)
#     print("Bot:", answer)

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

# on click of send button
# if st.button("Send") and user_input:
#     with st.spinner("Thinking..."):
#         answer = student_bot(user_input)

# for displaying full ans:
for q, a in st.session_state.conversation_history:
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

# for q, a in st.session_state.conversation_history:
#     st.markdown(
#         f"<p style='color:black'><b>You:</b> {q}</p>", unsafe_allow_html=True)
#     st.markdown(
#         f"<p style='color:black'><b>Bot:</b> {a}</p>", unsafe_allow_html=True)
# on click of clear button
if (st.button("Clear Chat")):
    st.session_state.conversation_history = []
    st.session_state.user_input_text = ""
    st.rerun()
