# decode-secret-message
Program written as part of coding test from DA.

# Decode Secret Message
 
A Python script that fetches a published Google Doc containing a table of `(x, y)` coordinates and Unicode characters, then prints the characters as a 2D grid to reveal a hidden message.
 
## How It Works
 
The input document contains a table with three columns:
 
| x-coordinate | Character | y-coordinate |
|--------------|-----------|--------------|
| 0            | █         | 0            |
| 0            | █         | 1            |
| 1            | ▀         | 1            |
 
Each row places one character at a position on a grid. When all the characters are printed at their positions, they form a message in uppercase letters.
 
The script works in two steps:
 
1. **`fetch_data(url)`** downloads the document and parses the table.
   - Fetches the page with `requests` and checks the request succeeded (`raise_for_status()`).
   - Decodes the response as UTF-8 so block characters such as `█` and `▀` come through correctly.
   - Parses the HTML with `BeautifulSoup`, finds the table, and loops over its `<tr>` rows, skipping the header row.
   - Reads each row's three `<td>` cells as the x value, the character, and the y value, converts x and y to integers, and stores them in a dictionary: `(x, y) -> character`.
2. **`decode_secret_msg(coordinates)`** prints the grid.
   - Finds the maximum x and y values to determine the grid size.
   - Loops over each row from `max_y` down to `0`, so `(0, 0)` ends up at the bottom-left, like a normal graph.
   - For each position in the row, looks up the character in the dictionary, using a space when there is none so the columns stay aligned.
   - Joins each row's characters into one string and prints it on its own line.
## Requirements
 
- Python 3.8+
- [`requests`](https://pypi.org/project/requests/)
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/)
## Setup
 
```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows (Command Prompt)
 
# Install dependencies
pip install requests beautifulsoup4
```
 
## Usage
 
```bash
python3 decode_grid.py
```
 
To decode a different document, change `DOCUMENT_URL` at the top of the script. The document must be published to the web (its URL contains `/pub`) and use the same table format described above.

## Example Output
```
█  █ ███
█  █  █ 
████  █ 
█  █  █ 
█  █ ███
```
