#  Web Scraper - News Headlines

A simple Python script to **automatically scrape top news headlines** from a public website and save them into a `.txt` file.  
This project uses the [`requests`](https://pypi.org/project/requests/) library to fetch HTML and [`BeautifulSoup`](https://pypi.org/project/beautifulsoup4/) to parse and extract `<h2>` or `<title>` tags.

---

##  Features
- Fetches HTML content from a news website (BBC News by default).
- Parses `<h2>` and `<title>` tags to extract headlines.
- Saves all collected headlines into `headlines.txt`.
- Simple, lightweight, and beginner-friendly.

---

##  Project Structure
- scrape_headlines.py # Main Python script.
- headlines.txt # Output file with scraped headlines(auto-generated).
- README.md # Project documentation.




---

##  Requirements
- Python 3.8+ (works with Python 3.11/3.12)
- Libraries:
  - `requests`
  - `beautifulsoup4`

Install them with:

```bash
pip install requests beautifulsoup4
