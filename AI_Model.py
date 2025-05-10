import requests
import streamlit as st
import time

# Hugging Face API setup
API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/deepseek-coder-1.3b-base"
headers = {"Authorization": "Bearer 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"}

# Send prompt to Hugging Face
def query_model(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"temperature": 0.2, "max_new_tokens": 300}
    }
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 503:
        st.warning("Model is loading... please wait ⏳")
        time.sleep(5)
        return query_model(prompt)
    elif response.status_code != 200:
        st.error(f"API error {response.status_code}: {response.text}")
        return None

    try:
        return response.json()
    except:
        st.error("Failed to parse response.")
        return None

# Streamlit UI
st.set_page_config(page_title="💻 AI Code Generator", layout="centered")
st.title("💻 AI Code Generator (via Hugging Face DeepSeek)")
st.markdown("Generate clean code from natural language prompts using free Hugging Face models.")

# Theme selection
theme = st.selectbox("Choose Theme:", ["Light", "Dark"])

# Apply working theme using HTML style block
def set_theme(theme):
    if theme == "Dark":
        st.markdown("""
            <style>
            html, body, [class*="css"] {
                background-color: #0e1117 !important;
                color: white !important;
            }
            textarea, input, select {
                background-color: #262730 !important;
                color: white !important;
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            html, body, [class*="css"] {
                background-color: white !important;
                color: black !important;
            }
            </style>
        """, unsafe_allow_html=True)

set_theme(theme)

# Prompt + Language Input
prompt = st.text_area("Enter your coding prompt:", height=150)
language = st.selectbox("Select programming language (for formatting)", ["Python", "C++", "JavaScript", "Java", "HTML", "Other"])

# Generate Button
if st.button("⚙️ Generate Code"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating code..."):
            result = query_model(prompt)
            if result and isinstance(result, list) and "generated_text" in result[0]:
                raw_code = result[0]["generated_text"]
                cleaned_code = raw_code.replace(prompt, "").strip()
                st.code(cleaned_code, language=language.lower())

                # Add download button
                file_extension = {
                    "Python": "py", "C++": "cpp", "JavaScript": "js",
                    "Java": "java", "HTML": "html", "Other": "txt"
                }.get(language, "txt")
                st.download_button("📥 Download Code", cleaned_code, file_name=f"generated_code.{file_extension}")
            else:
                st.error("❌ The model did not return proper code.")
