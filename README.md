# 🧠 AI Ops Toolkit

This repository contains three small projects demonstrating practical applications of **AI, automation, and web integration** — combining web scraping, telephony automation, and generative AI.

Each project showcases a distinct technical capability:
data extraction, automated voice operations, and AI-driven content generation.

---

## 📘 1. LinkedIn Profile Scraper

**Goal:**
Scrape and collect public LinkedIn profile data into a CSV file.

**Overview:**

* Automates browser actions using **Selenium** and **Chrome WebDriver**.
* Uses a **test LinkedIn account** for login and controlled access.
* Scrapes 20 random profile URLs (`linkedin.com/in/xxxxxx`) for public info like name, title, and company.
* Stores extracted data in a structured CSV format.
* Implements **rotating proxies** and **user-agent randomization** to reduce blocking risk.

**Tech Stack:** Python, Selenium, BeautifulSoup, Chrome Web Driver, Pandas

---

## 📞 2. Autodialer (Ruby on Rails + Twilio)

**Goal:**
Build a voice automation system that can place phone calls programmatically and optionally use AI for generating call scripts.

**Overview:**

* A **Ruby on Rails app** integrated with the **Twilio Voice API**.
* Accepts commands like `call +91XXXXXXXXXX` or a bulk list of 100 numbers.
* Makes automated calls (for testing, uses toll-free or demo numbers like 1800-XXX-XXXX).
* Displays call logs: success, failure, and unanswered calls.
* Optional **AI prompt integration** to dynamically generate call dialogue or scripts.

**Note:**
Outbound automated calling via Twilio or foreign VoIP is **restricted under TRAI/DoT telecom laws in India**,
and international calls from US numbers can incur high testing costs — this app is therefore **demonstrative only**.

**Tech Stack:** Ruby on Rails, Twilio API, Gemini (for AI voice script)

---

## ✍️ 3. AI Blog Generator

**Goal:**
Generate technical articles automatically from a list of topic titles using AI.

**Overview:**

* Built with **Streamlit** and **Google Gemini API**.
* Allows you to input one or multiple titles (e.g., *Optimizing Python with NumPy*).
* Generates fully formatted, markdown-based blogs with introduction, sections, and conclusion.
* Automatically saves generated articles to `/output/blogs/`.
* Ideal for automating content pipelines or seeding technical blogs.

**Tech Stack:** Python, Streamlit, Google Gemini API

---

## 🧩 Folder Structure

```
AI_Automation_Assignment/
├── linkedin_scraper/       # LinkedIn scraping automation
├── autodialer/             # Voice call automation app
├── ai_blog_generator/         # AI-powered content generator
└── README.md               # Master project overview (this file)
```

---

## 🧑‍💻 Author
```bash
**Anurag Mishra**
AI & ML Engineer | Data Scientist
📧 [officiallyanurag1@gmail.com](mailto:officiallyanurag1@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/anuragmishra02/)
💻 [GitHub](https://github.com/OPanurag)
```
---

## ⚖️ Disclaimer

This project is for **educational and research purposes only**.