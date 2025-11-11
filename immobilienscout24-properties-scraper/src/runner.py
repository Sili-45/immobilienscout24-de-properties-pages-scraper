thonimport requests
from extractors.property_parser import parse_property
from outputs.exporters import export_data

def run_scraper(urls):
    properties_data = []
    
    for url in urls:
        property_data = parse_property(url)
        if property_data:
            properties_data.append(property_data)

    export_data(properties_data)

if __name__ == "__main__":
    input_urls = ["https://www.immobilienscout24.de/expose/12345", "https://www.immobilienscout24.de/expose/67890"]
    run_scraper(input_urls)