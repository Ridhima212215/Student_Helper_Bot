import streamlit as st
from openai import OpenAI

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


st.title("📝 Text Summarizer")
st.write("Paste your text below and get a concise summary.")

text_to_summarize = st.text_area(
    "Enter text to summarize", height=300, key="summarizer_text")
if st.button("Summarize Text"):
    if text_to_summarize.strip():
        with st.spinner("Summarizing..."):
            summary = summarize_text(text_to_summarize)
            st.success("Summary:")
            st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
