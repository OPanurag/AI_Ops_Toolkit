# 🧠 AI Blog Generator (Gemini + Streamlit)

> An AI-powered blog content generator with a simple web interface — built using **Google Gemini API** and **Streamlit**.
> Type your blog titles, click generate, and instantly get full-length, Markdown-formatted articles saved locally.

---

## 🚀 Features

* ✨ **One-click blog generation** via Streamlit web UI
* 📘 **Markdown-formatted articles** with headings, code blocks, and summaries
* 🔒 **Secure API key management** using `.env` file (no hardcoding)
* 🧩 **Powered by Google Gemini API** for advanced language generation
* 💾 **Automatic saving** of generated articles in `/output/blogs/`
* ⚙️ **Modular and extensible** — can be integrated with CMS or automation tools
* 🧱 **Streamlit frontend** for easy non-technical usage

---

## 📁 Directory Structure

```
AI_Ops_Toolkit/
├── ai_blog_generator/
│   ├── ai_blog_generator.py     # Streamlit web app
│   ├── .env                     # Stores your Gemini API key (excluded from Git)
│   ├── output/
│   │   └── blogs/               # Generated Markdown blog files
│   ├── prompts/                 # (Optional) Custom prompt templates
│   └── README.md                # This documentation
├── venv/                        # Virtual environment (recommended)
└── requirements.txt             # Python dependencies
```

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<OPAnurag>/AI_Ops_Toolkit.git
cd AI_Ops_Toolkit/ai_blog_generator
```

### 2️⃣ Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate       # macOS/Linux
# OR
venv\Scripts\activate          # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, create one with:

```bash
google-generativeai==0.8.5
python-dotenv==1.0.1
streamlit==1.51.0
```

Then install:

```bash
pip install -r requirements.txt
```

### 4️⃣ Create your `.env` file

In the `ai_blog_generator` folder, create a file named `.env`:

```bash
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

> ⚠️ **Important:** Never share or commit your `.env` file.

---

## 🧠 How It Works

The Streamlit app:

1. Loads your Gemini API key from `.env`.
2. Takes one or more blog titles from the text box.
3. Generates detailed, structured articles using the Gemini model (`gemini-2.5-flash`).
4. Saves each article to `/output/blogs/<title>.md`.
5. Displays the generated article in a preview expander.

---

## ▶️ Running the Application

Run the app from inside your virtual environment:

```bash
streamlit run ai_blog_generator.py
```

or to avoid system path confusion:

```bash
python -m streamlit run ai_blog_generator.py
```

Then open the automatically displayed URL:

```
http://localhost:8501
```

---

## 💻 Using the App

1. **Enter blog titles** (one per line) in the input box.
2. Click **🚀 Generate Blogs**.
3. Watch as your blogs are generated and previewed in real time.
4. Each blog is saved in:

   ```
   output/blogs/<blog_title>.md
   ```
5. You can open the Markdown file directly or copy the content from the Streamlit preview.

---

## 📝 Example Output

**Generated File:**
`output/blogs/optimizing_python_with_numpy.md`

````markdown
# Optimizing Python with NumPy

## Why NumPy Matters
NumPy is the foundation for numerical computation in Python...

## Vectorization and Performance
By replacing loops with NumPy operations, performance improves dramatically.

## Example
```python
import numpy as np
a = np.arange(1e6)
b = np.arange(1e6)
result = a + b
````

## Conclusion

NumPy provides not just speed but also scalability and cleaner syntax.

````

---

## ⚙️ Environment Variables

| Variable | Description | Required |
|-----------|--------------|-----------|
| `GEMINI_API_KEY` | Your Google Gemini API key | ✅ Yes |

**To set manually (optional):**
```bash
export GEMINI_API_KEY="your_api_key_here"
````

---

## 🧩 Customization

You can create prompt templates in `prompts/` to control tone or style.

Example:

```
prompts/
├── tutorial.txt
└── opinion_piece.txt
```

Then modify the `generate_blog()` function to read the desired template instead of the default inline prompt.

---

## 🧪 Troubleshooting

**Issue:** `ModuleNotFoundError: No module named 'google.generativeai'`
✅ Fix: Make sure it’s installed in your venv:

```bash
pip install google-generativeai
```

**Issue:** Streamlit runs from global Python
✅ Fix: Run Streamlit via venv’s Python:

```bash
python -m streamlit run ai_blog_generator.py
```

**Issue:** API key not found
✅ Fix: Check your `.env` file and ensure `GEMINI_API_KEY` is correctly set.

---

## 🧠 Future Enhancements

* Add **SEO keyword extraction**
* Integrate **AI-powered blog summarization**
* Export directly to **CMS (WordPress, Ghost, Hashnode)**
* Add **scheduled auto-generation** (via CRON or API)
* Theme customization for blog output

---

## 👨‍💻 Author

**Anurag Mishra**
AI & ML Engineer | Data Scientist
📧 [officiallyanurag1@gmail.com](mailto:officiallyanurag1@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/anuragmishra02/)
💻 [GitHub](https://github.com/OPanurag)

---

## 🧩 License

MIT License © 2025 — Free for educational and commercial use with attribution.