thonimport requests
from bs4 import BeautifulSoup

def parse_property(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.find('h1', {'class': 'headline'}).text.strip()
        description = soup.find('div', {'class': 'description'}).text.strip()
        price = soup.find('div', {'class': 'price'}).text.strip()
        construction_date = soup.find('div', {'class': 'construction-year'}).text.strip()
        
        property_data = {
            "title": title,
            "description": description,
            "price": price,
            "construction_date": construction_date,
        }
        return property_data
    except Exception as e:
        print(f"Error parsing {url}: {e}")
        return None