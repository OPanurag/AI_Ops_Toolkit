"""
A simple AI-powered blog generator using the Gemini API.

It:
- Reads blog titles (with optional details) from titles.txt
- Generates full blog content via Gemini API
- Saves each blog as a Markdown file under output/blogs/
- Logs progress and errors

Usage:
    python ai_blog_generator/ai_blog_generator.py
"""

import os
import time
import random
import google.generativeai as genai

from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# ================= CONFIG =================
TITLES_FILE = os.path.join(os.path.dirname(__file__), "titles.txt")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output", "blogs")
PROMPTS_DIR = os.path.join(os.path.dirname(__file__), "prompts")

# Load API key from env var
API_KEY = os.getenv("GEMINI_API_KEY")  # set in .env file
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not set. Please create a .env file.")

genai.configure(api_key=API_KEY)

MODEL_NAME = "gemini-2.5-flash"  # You can also use "gemini-pro" or "gemini-1.5-pro"
MIN_SLEEP = 3
MAX_SLEEP = 6
# ==========================================


def load_titles():
    """Read titles from titles.txt"""
    with open(TITLES_FILE, "r") as f:
        titles = [line.strip() for line in f if line.strip()]
    return titles


def generate_prompt(title):
    """Generate a clean prompt for Gemini"""
    base_prompt = f"""
You are a technical writer specializing in programming tutorials and deep dives.
Write a detailed, well-structured, SEO-optimized blog article on the following topic:
"{title}"

The article must:
- Be at least 800 words
- Contain clear sections with Markdown headers (##, ###)
- Include examples, code snippets, and practical explanations
- Avoid fluff, keep a professional tone
- End with a short summary and takeaway points
"""
    return base_prompt.strip()


def generate_blog(title):
    """Call Gemini API to generate a blog post."""
    prompt = generate_prompt(title)
    model = genai.GenerativeModel(MODEL_NAME)
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"⚠️ Error generating blog for '{title}': {e}")
        return None


def save_blog(title, content):
    """Save blog as Markdown file."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    safe_name = title.lower().replace(" ", "_").replace("/", "_")[:50]
    file_path = os.path.join(OUTPUT_DIR, f"{safe_name}.md")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{content}")

    print(f"✅ Saved: {file_path}")
    return file_path


def main():
    print("🚀 Starting AI Blog Generator...")
    titles = load_titles()

    if not titles:
        print("❌ No titles found in titles.txt")
        return

    print(f"🧠 Loaded {len(titles)} titles from titles.txt\n")

    for i, title in enumerate(titles, 1):
        print(f"[{i}/{len(titles)}] Generating blog for: {title}")
        content = generate_blog(title)
        if content:
            save_blog(title, content)
        else:
            print(f"❌ Failed to generate blog for {title}")
        time.sleep(random.uniform(MIN_SLEEP, MAX_SLEEP))

    print("\n🎉 All blogs generated successfully!")


if __name__ == "__main__":
    main()
