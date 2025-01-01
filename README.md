# holyscrap

# Python Scraping Tech Profiles (generic)

This Python script allows you to **scrape technology profiles** (mostly personal portfolio pages) to extract public information such as **skills**, **work experience**, and more. The project uses popular libraries like **Selenium**, **BeautifulSoup**, and **User-Agent Rotation** to explore web pages; dynamically interact with elements, and avoid being blocked by servers - **/!\** Internet is something almost alive so this script is not final. It should be refined and updated regularly. 

### Why this script?

This script is an introduction to designing your own research approach. The challenge was to be able to browse the sources without using an API. Today, the Internet is full of API and it is becoming complicated for individuals who do not have the money or the necessary skills to do precise research.

## Prerequisites

Before start, please load the following elements:

- **Python 3.#** : I had thought about Rust or Haxe. But Python seems more flexible to me for a first approach.
- **Selenium** : To control a web browser in automatic mode.
- **BeautifulSoup4** : To `parse` HTML pages & extract relevant information.
- **WebDriver (Chrome)** : To control the Chrome browser via Selenium; **/!\** you have to understand that Chrome is very alert to scraping. That's why I voluntarily excluded Chrome from my script after several unsuccessful attempts. However, you can try your luck.
- **User-Agent Rotation** : To simulate a real user & avoid blocking by servers.

You can install these dependencies via pip - `py -m pip install` :

```bash
py -m pip install selenium beautifulsoup4 fake-useragent
```
---------------------------------------------------

**1.Import modules**
```
import requests
from bs4 import BeautifulSoup
```
**requests** : Used to send HTTP requests. Allows you to send a GET request to DuckDuckGo to get the content of a web page.

**BeautifulSoup** : From the bs4 library. Used to "parse" HTML content & extract specific information (like links, titles, etc.).

---------------------------------------------------
**2.Main fonction**
```
def duckduckgo_search_portfolios(keyword, num_results=10):
```
_duckduckgo_search_portfolios function takes two parameters_
**keyword** : Keyword you want to search for on DuckDuckGo.

**num_results** : Number of results to return (default is 10).

---------------------------------------------------
**3.Request building**
```
query = f"{keyword} site:dev OR site:io OR site:me"
```
This line creates a query text string --> formatted search query for DuckDuckGo.

The format site:dev OR site:io OR site:me means that the search will be limited to results from sites with the .dev, .io, or .me extensions. This is useful for targeting developer portfolios or online profiles that are on these popular domain types. in fact, you can adapt the code for any sector.

---------------------------------------------------
**4. DuckDuckGo URL creation**
```
url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
```
URL of the DuckDuckGo search results page by replacing spaces with + (as required by URL encoding for an HTTP request).

---------------------------------------------------
**5.Header HTTP requests**
```
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
```
User-Agent header --> used to impersonate a web browser --> the request is not (will not) blocked by DuckDuckGo. Without this header, some pages might refuse the connection, thinking that the request comes from a bot.

---------------------------------------------------
**6.Sending GET request & retrieving the response**
```
response = requests.get(url, headers=headers)
```
Sends GET request to the DuckDuckGo URL w/ the specified headers, then --> retrieves the response.

---------------------------------------------------
**7.Request verification**
```
if response.status_code == 200:
```
Checks HTTP status code; if the response is 200, which means the request was successful and the page content is available.

---------------------------------------------------
**8.HTML page content analysis**
```
soup = BeautifulSoup(response.text, 'html.parser')
```
BeautifulSoup --> used to "parse" HTML content of the response obtained. The response text (HTML content) is passed to BeautifulSoup to facilitate information = extraction facilitator.

---------------------------------------------------
**9.Extracting links**
```
links = []
        for a in soup.find_all('a', class_='result__a', href=True):
            link = a['href']
            if link:
                links.append(link)
```
**soup.find_all('a', class_='result__a', href=True)** : Line searches for all <a> elements (links) in the page that have the CSS class result__a and an href attribute (which contains the URL of the link).

**link = a['href']** : Gets the value of the href attribute (i.e. the URL) for each link.
_If the URL is valid, it is added to the links list._

---------------------------------------------------
**10.Return the first results**
```
        return links[:num_results]
```
Once all the links are extracted, the function returns the first num_results links (the results are limited to a given number, by default 10).

---------------------------------------------------
**11.Error management**
```
else:
        print("Error retrieving results.")
        return []
```
If the request fails (if the HTTP status code is not 200) --> an error message is printed & the function returns an empty list.

---------------------------------------------------
**12.e.g. function utilization**
```
keyword = "backend developer portfolio"
profiles = duckduckgo_search_portfolios(keyword, num_results=5)
```
Define keyword to search for (e.g. "backend developer portfolio") & call the duckduckgo_search_portfolios function to get 5 results.

---------------------------------------------------
**13.Display the results**
```
if profiles:
    for profile in profiles:
        print(f"URL: {profile}")
else:
    print("No profile found.")
```
If profiles (links) are found --> displayed on the screen, one by one, with the prefix URL:.

If no profiles are found --> the message "No profile found." is printed.

---------------------------------------------------
## Process Summary
- *User* enters a keyword and, optionally, a desired number of results.
- *Function* creates a DuckDuckGo query to search for developer portfolios (or other profiles based on the keyword).
- *Query* is sent to DuckDuckGo via an HTTP request.
- *Content* of the DuckDuckGo HTML page is "parsed" to extract links from the results.
- *Links* are returned & displayed to the user.

**Script therefore makes it easy to search for developer portfolios or online profiles (or other keywords) on DuckDuckGo and display the results as links.**




.
.
.
.


矢筒に別の矢が入った。
