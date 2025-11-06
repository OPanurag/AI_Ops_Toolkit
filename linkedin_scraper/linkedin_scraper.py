"""
selenium_scraper.py
A simple Selenium-based LinkedIn scraper (for educational/testing use).

It:
- Reads LinkedIn profile URLs from urls.txt
- Opens each in Chrome using Selenium
- Extracts name, headline, location, and about (best-effort)
- Saves results to output/linkedin_profiles.csv
"""

import os
import time
import random
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# ================= CONFIG =================
# URLS_FILE = "linkedin_scraper/urls.txt"
OUTPUT_DIR = "output"
URLS_FILE = os.path.join(os.path.dirname(__file__), "urls.txt")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "output", "linkedin_profiles.csv")
# OUTPUT_FILE = os.path.join(OUTPUT_DIR, "linkedin_profiles.csv")

HEADLESS = True     # Set to False if you want to see the browser
LOGIN_URL = "https://www.linkedin.com/login"
EMAIL = "etest2260@gmail.com"      # <--- Use test account only
PASSWORD = "test_email0987"            # <--- Use test account only

MIN_SLEEP = 3
MAX_SLEEP = 7
# ==========================================


def setup_driver():
    """Initialize Selenium Chrome driver with sensible defaults."""
    chrome_options = Options()
    if HEADLESS:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.7444.60 Safari/537.36"
    )

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def linkedin_login(driver):
    """Logs in to LinkedIn using a test account (if credentials provided)."""
    if not EMAIL or not PASSWORD:
        print("Skipping login (no credentials provided).")
        return
    print("Logging in to LinkedIn...")
    driver.get(LOGIN_URL)
    time.sleep(2)
    try:
        email_input = driver.find_element("id", "username")
        password_input = driver.find_element("id", "password")
        login_button = driver.find_element("xpath", "//button[@type='submit']")

        email_input.send_keys(EMAIL)
        password_input.send_keys(PASSWORD)
        login_button.click()
        time.sleep(3)
        print("Login successful (if credentials are valid).")
    except Exception as e:
        print(f"Login failed or not needed: {e}")


def extract_fields_from_html(html):
    """Parse HTML using BeautifulSoup to extract key profile data."""
    soup = BeautifulSoup(html, "html.parser")

    def safe_text(selectors):
        for s in selectors:
            el = soup.select_one(s)
            if el and el.get_text(strip=True):
                return el.get_text(strip=True)
        return "N/A"

    name = safe_text([".text-heading-xlarge", "h1"])
    headline = safe_text([".text-body-medium.break-words", ".pv-top-card-section__headline"])
    location = safe_text([".text-body-small.inline.t-black--light.break-words", ".pv-top-card-section__location"])
    about = safe_text(["section.pv-about-section p", "#about", ".display-flex.ph5.pv3 span"])

    return {"name": name, "headline": headline, "location": location, "about": about}


def scrape_profiles():
    """Main scraper logic."""
    driver = setup_driver()
    linkedin_login(driver)

    # read urls
    with open(URLS_FILE, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    results = []

    print(f"Starting scrape for {len(urls)} profiles...")

    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] Visiting: {url}")
        try:
            driver.get(url)
            time.sleep(random.uniform(MIN_SLEEP, MAX_SLEEP))
            html = driver.page_source
            data = extract_fields_from_html(html)
            data["url"] = url
            results.append(data)
            print(f"   -> {data['name']} | {data['headline'][:50]}")
        except Exception as e:
            print(f"   -> Error: {e}")
            results.append({
                "url": url,
                "name": "ERROR",
                "headline": str(e),
                "location": "N/A",
                "about": "N/A"
            })

    driver.quit()

    df = pd.DataFrame(results, columns=["url", "name", "headline", "location", "about"])
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n✅ Done! Saved {len(results)} profiles to {OUTPUT_FILE}")


if __name__ == "__main__":
    scrape_profiles()
