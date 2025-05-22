
# 🌍 LangChain LLM Translator

A simple app that translates text into **French** using **LangChain**, **Groq's Gemma2-9b-It model**, **FastAPI**, and **Streamlit**.

---

## 🚀 Features

- LangChain pipeline with prompt → LLM → output
- FastAPI backend using `langserve`
- Streamlit frontend for user interaction
- API key management with `.env`

---

## 📁 Project Structure

```
langchain-llm-translator/
├── serve.py            # FastAPI backend
├── client.py           # Streamlit frontend
├── simplellmLCEL.ipynb # Notebook for testing
├── requirements.txt    # Python dependencies
└── README.md
```

---

## ⚙️ Setup & Usage

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Create `.env` file**  
   ```env
   GROQ_API_KEY=your_groq_api_key
   ```

3. **Run backend**  
   ```bash
   python serve.py
   ```

4. **Run frontend**  
   ```bash
   streamlit run client.py
   ```

---

## 📌 Notes

- Add your Groq API key in `.env`
- The app translates to French by default

---

## 🛠️ Built With

- LangChain
- FastAPI
- Streamlit
- Groq LLM

---

## 🧠 Author

Made by [Arunangshu Prasad Bhattacharya](https://github.com/ap-bhattacharya)

---
