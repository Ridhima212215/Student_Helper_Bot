# Student Helper Bot

👩‍🎓 **Student Helper Bot** is a Streamlit-based application designed to assist students with various tasks, including answering questions, summarizing text. It leverages OpenAI's GPT models to provide intelligent and interactive features.

---

## Features

### 1. **Chatbot**
- Ask any academic or general questions.
- Get concise and helpful answers powered by OpenAI.

### 2. **Text Summarizer**
- Paste any text (e.g., lecture notes, articles) and get a concise summary.
- Ideal for quick reviews and understanding large blocks of text.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API Key

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Ridhima212215/Student_Helper_Bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Student_Helper_Bot
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your OpenAI API key:
   - Create a `.streamlit/secrets.toml` file in the project directory.
   - Add the following content:
     ```toml
     OPENAI_API_KEY="your-api-key-here"
     ```

5. Run the app locally:
   ```bash
   streamlit run app.py
   ```

---

## Deployment

This app is deployed on **Streamlit Cloud**. You can access it using the following URL:

👉 [Student Helper Bot](https://studentapperbot-c4df2cedj7hnizrw9mwtd3.streamlit.app)

---

## Folder Structure

```
Student_Helper_Bot/
├── app.py                # Main chatbot application
├── pages/                # Additional features as separate pages
│   ├── The Summarizer.py # Text summarizer feature
├── assets/               # Static assets (e.g., background images)
│   └── b4.jpg            # Background image
├── requirements.txt      # Python dependencies
├── .streamlit/           # Streamlit configuration
│   └── secrets.toml      # OpenAI API key (ignored by Git)
└── README.md             # Project documentation
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

---

## Contact

For questions or feedback, please contact [Ridhima212215](https://github.com/Ridhima212215).
