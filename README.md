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

.
.
.
.


矢筒に別の矢が入った。
