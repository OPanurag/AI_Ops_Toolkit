# 🧠 LinkedIn Profile Scraper (Educational Use Only)
```
A simple **Selenium-based LinkedIn profile scraper** built for educational and testing purposes.  
It automates Chrome using Selenium, extracts profile data from given LinkedIn URLs, and saves the results into a CSV file incrementally.
```
---

## 🚀 Features

- Reads LinkedIn profile URLs from `urls.txt`
- Logs into LinkedIn using a test account (optional)
- Opens each profile in a headless Chrome browser
- Extracts:
  - Name  
  - Headline  
  - Location  
  - About section
- Saves results **incrementally** to `output/linkedin_profiles.csv`  
- Handles failures gracefully — any broken links or timeouts are logged with `"ERROR"`

---

## 🧩 Project Structure

````bash

AI_Ops_Toolkit/
└── linkedin_scraper/
        ├── linkedin_scraper.py        # Main Selenium scraper script
        ├── urls.txt                   # List of LinkedIn profile URLs
        ├── output/
        │   └── linkedin_profiles.csv  # Output file generated after run
        └── README.md                  # Project documentation

````

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/OPAnurag/AI_Ops_Toolkit.git
cd AI_Ops_Toolkit/linkedin_scraper
````

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install selenium webdriver-manager pandas beautifulsoup4
```

Make sure **Google Chrome** is installed on your system.
You can verify it using:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --version
```

---

## ▶️ Usage

### Step 1: Add Profile URLs

Create a file named `urls.txt` in the `linkedin_scraper` folder and add one LinkedIn profile URL per line:

```
https://www.linkedin.com/in/sundar-pichai
https://www.linkedin.com/in/satyanadella
https://www.linkedin.com/in/arvindkrishna
```

### Step 2: Run the Scraper

Execute this command from the **project root**:

```bash
python linkedin_scraper/linkedin_scraper.py
```

This will:

* Launch a headless Chrome browser
* Optionally log into LinkedIn using your provided test credentials
* Scrape each profile in sequence
* Save extracted data incrementally into `output/linkedin_profiles.csv`

---

## 🧾 Output Format

The scraper saves output in CSV format with the following columns:

| url | name | headline | location | about |
| --- | ---- | -------- | -------- | ----- |

Example output:

```
https://www.linkedin.com/in/sundar-pichai, Sundar Pichai, CEO at Google, California, United States, Passionate about building useful technology.
https://www.linkedin.com/in/satyanadella, Satya Nadella, Chairman and CEO at Microsoft, Redmond, Washington, Focused on AI and innovation.
```

---

## ⚡ Key Highlights

* **Incremental Writing:** Each profile’s data is appended immediately after extraction (no data loss even if interrupted).
* **Headless Mode:** Default setting allows scraping without opening a browser window.
* **Lightweight & Safe:** Uses official ChromeDriver via `webdriver-manager`, ensuring compatibility with your installed Chrome version.
* **Extensible:** You can modify selectors in `extract_fields_from_html()` to capture more data like experience, education, etc.

---

## 🧠 Technical Notes

* Fake user agents are **optional** — this script already includes a real Chrome user agent for safe execution.
* For large-scale or production scraping, use **LinkedIn’s official APIs** or **Sales Navigator Export**, as scraping may violate LinkedIn’s Terms of Service.
* Always use a **test or dummy LinkedIn account**.

---

## 🧰 Troubleshooting

**1. Chrome not found error:**
Check that Chrome is installed and accessible at
`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` (macOS).
For Linux or Windows, update the `webdriver-manager` installation automatically.

**2. Login not working:**
Ensure that the `EMAIL` and `PASSWORD` constants in the script are updated with valid **test credentials**.

**3. CAPTCHA or access denied:**
LinkedIn may block automated requests. Add random delays or switch to manual login once.

---

## 🧑‍💻 Author
```bash
**Anurag Mishra**
AI & ML Engineer | Data Scientist
📧 Email --> officiallyanurag1@gmail.com
🔗 LinkedIn --> https://www.linkedin.com/in/anuragmishra02/
💻 GitHub --> https://github.com/OPanurag
```
---

## ⚖️ Disclaimer

This project is for **educational and research purposes only**.
Scraping LinkedIn or other platforms without permission may violate their Terms of Service.
Use responsibly.