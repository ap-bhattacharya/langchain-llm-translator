import requests
import streamlit as st

def get_groq_response(input_text):
    json_body = {
        "input": {
            "language": "French",  # You can make this dynamic if needed
            "text": input_text
        }
    }

    response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)

    return response.json()

## Streamlit app
st.title("LLM Application Using LCEL")
input_text = st.text_input("Enter the text you want to convert to French")

if input_text:
    st.write(get_groq_response(input_text))
