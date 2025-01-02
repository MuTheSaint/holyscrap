import requests
from bs4 import BeautifulSoup

def duckduckgo_search_portfolios(keyword, num_results=20):
    query = f"{keyword} site:dev OR site:io OR site:me"
    url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
    
# Request GET --> obtenir le contenu de la page

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:

# Parser page content

        soup = BeautifulSoup(response.text, 'html.parser')
        
# Vamp the results

        links = []
        for a in soup.find_all('a', class_='result__a', href=True):
            link = a['href']
            if link:
                links.append(link)
        
        return links[:num_results]
    else:
        print("Error retrieving results.")
        return []

# Ex sample

keyword = "backend developer japan portfolio"
profiles = duckduckgo_search_portfolios(keyword, num_results=5)

if profiles:
    for profile in profiles:
        print(f"URL: {profile}")
else:
    print("No profile found.")
