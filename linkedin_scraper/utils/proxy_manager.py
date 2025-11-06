from fake_useragent import UserAgent
import random

class ProxyManager:
    """Handles random user-agent generation and potential proxy rotation."""

    def __init__(self):
        self.ua = UserAgent()
        # Optional: maintain a small pool of free proxies
        self.proxies = [
            # "http://username:password@ip:port",
            # "https://ip:port"
        ]

    def get_headers(self):
        return {"User-Agent": self.ua.random}

    def get_proxy(self):
        if not self.proxies:
            return None
        return random.choice(self.proxies)
