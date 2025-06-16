import streamlit as st
import google.generativeai as genai

# --- Gemini API Key Configuration ---
API_KEY = "Your API Key"
genai.configure(api_key=API_KEY)

# --- Model Setup ---
MODEL_NAME = "gemini-1.5-flash-latest"

try:
    model = genai.GenerativeModel(
        MODEL_NAME,
        system_instruction=(
            "You are an AI Code Generator. Your task is to generate clean, efficient, and well-commented code "
            "based on the user's prompt and programming language. Only output raw code."
        )
    )
except Exception as e:
    st.error(f"Model initialization failed: {e}")
    st.stop()

# --- Streamlit App Configuration ---
st.set_page_config(page_title="🤖 AI Code Generator", page_icon="💻", layout="centered")

st.title("💻 AI Code Generator (Gemini)")
st.markdown("Create clean and efficient code from natural language prompts using Google Gemini!")

# --- User Input ---
prompt = st.text_area("📝 Describe what you want the code to do", height=150)
language = st.selectbox("💡 Choose Programming Language", ["Python", "JavaScript", "C++", "Java", "Go", "auto"])

# --- Generate Code Button ---
if st.button("🚀 Generate Code"):
    if not prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        st.info("Generating code... Please wait ⏳")
        try:
            full_prompt = (
                f"Generate {language} code for the following task: {prompt}"
                if language.lower() != "auto"
                else f"Generate code for the following task: {prompt}. Try to infer the language."
            )

            response = model.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=2048,
                    temperature=0.4
                ),
                safety_settings={
                    genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT: genai.types.HarmBlockThreshold.BLOCK_ONLY_HIGH,
                    genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH: genai.types.HarmBlockThreshold.BLOCK_ONLY_HIGH,
                    genai.types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: genai.types.HarmBlockThreshold.BLOCK_ONLY_HIGH,
                    genai.types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: genai.types.HarmBlockThreshold.BLOCK_ONLY_HIGH,
                }
            )

            generated_code = response.text.strip()
            st.success("✅ Code generated successfully!")
            st.code(generated_code, language=language.lower() if language.lower() != "auto" else "python")

            # --- Optional Download Button ---
            file_ext = {
                "Python": "py", "JavaScript": "js", "C++": "cpp", "Java": "java", "Go": "go", "auto": "txt"
            }.get(language, "txt")

            st.download_button(
                label="📥 Download Code",
                data=generated_code,
                file_name=f"generated_code.{file_ext}",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"❌ Error generating code: {e}")