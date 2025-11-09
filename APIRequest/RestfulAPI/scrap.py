import requests
from bs4 import BeautifulSoup


# Function to fetch HTML content from the provided URL
def fetch_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.text


# Function to extract product data from the HTML using BeautifulSoup
def extract_product_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    products = []
    results = soup.find_all('div', {'data-component-type': 's-search-result'})

    for result in results:
        try:
            name = result.find('h2').text.strip()
            price = result.find('span', {'class': 'a-price'}).find('span', {'class': 'a-offscreen'}).text.strip()
            products.append({'name': name, 'price': price})
        except Exception as e:
            print('Error:', e)

    return products


# Main function to search for a product on Amazon and scrape its data
def main():
    search_query = 'laptop'  # Replace with the product you want to search for
    url = f'https://www.amazon.com/s?k={search_query.replace(" ", "+")}'

    html = fetch_html(url)
    data = extract_product_data(html)

    for product in data:
        print(product)


if __name__ == '__main__':
    main()
