import requests
from bs4 import BeautifulSoup

DOCUMENT_URL = "ADD YOUR URL"
REQUEST_TIMEOUT_SECONDS = 10
RESPONSE_ENCODING = "utf-8"

def fetch_data(url):
  """
    Retrieves and parses the data in the document url
    Returns a dict mapping (x, y) => char
  """
  response = requests.get(url, timeout=REQUEST_TIMEOUT_SECONDS)
  response.raise_for_status()
  response.encoding = RESPONSE_ENCODING
  

  soup = BeautifulSoup(response.text, "html.parser")
  rows = soup.find("table").find_all("tr")[1:]

  coordinates = {}
  for tr in rows:
    x, char, y = (td.get_text(strip=True) for td in tr.find_all("td"))
    coordinates[(int(x),int(y))] = char

  return coordinates

def decode_secret_msg(coordinates):
  """
    Print the Unicode characters as a 2D grid 
  """
  max_x = max(x for x, _ in coordinates)
  max_y = max(y for _, y in coordinates)

  for y in range(max_y, -1, -1):
    print("".join(coordinates.get((x, y), " ") for x in range(max_x + 1)))

decode_secret_msg(fetch_data(DOCUMENT_URL))