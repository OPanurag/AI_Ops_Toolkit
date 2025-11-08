import os
import time
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from pathlib import Path

# ================= CONFIGURATION =================
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    st.error("❌ GEMINI_API_KEY not found in .env file.")
    st.stop()

genai.configure(api_key=API_KEY)
MODEL_NAME = "gemini-2.5-flash"
OUTPUT_DIR = Path(__file__).parent / "output" / "blogs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
# ==================================================


def generate_blog(title: str, model_name: str = MODEL_NAME) -> str:
    """Generate blog content for a given title using Gemini API."""
    prompt = (
        f"Write a detailed, well-structured technical article on '{title}'. "
        f"Focus on clarity, examples, and practical insights. "
        f"Use markdown formatting (### headings, lists, code blocks, etc.) "
        f"Include an introduction and conclusion."
    )

    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return response.text.strip()


def save_blog(title: str, content: str):
    """Save generated blog to markdown file."""
    safe_name = "_".join(title.lower().split())
    filepath = OUTPUT_DIR / f"{safe_name}.md"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath


# ================= STREAMLIT UI ===================
st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="🧠",
    layout="wide",
)

st.title("🧠 AI Blog Generator (Gemini Powered)")
st.markdown(
    "Type one or more blog titles below (one per line), and click **Generate Blogs** to create AI-written articles."
)

titles_input = st.text_area(
    "Enter blog titles:",
    placeholder="e.g.\nOptimizing Python with NumPy\nDeep Learning in Edge Devices\nBuilding APIs with FastAPI",
    height=180,
)

generate_button = st.button("🚀 Generate Blogs")

if generate_button:
    titles = [t.strip() for t in titles_input.split("\n") if t.strip()]
    if not titles:
        st.warning("Please enter at least one title.")
    else:
        progress = st.progress(0)
        total = len(titles)
        results = []

        for i, title in enumerate(titles, 1):
            with st.spinner(f"Generating blog {i}/{total}: {title}"):
                try:
                    content = generate_blog(title)
                    path = save_blog(title, content)
                    st.success(f"✅ {title} saved → {path.name}")
                    with st.expander(f"📘 Preview: {title}"):
                        st.markdown(content)
                    results.append((title, path))
                except Exception as e:
                    st.error(f"Failed to generate '{title}': {e}")
                time.sleep(2)
                progress.progress(i / total)

        st.balloons()
        st.markdown("### 🎉 Generation Complete!")
        for title, path in results:
            st.markdown(f"- [{title}]({path})")

st.markdown("---")
st.caption("Built with Streamlit + Google Gemini | AI Ops Toolkit")
