import requests
from bs4 import BeautifulSoup
import json

response = requests.get("https://stockx.com/sneakers")
