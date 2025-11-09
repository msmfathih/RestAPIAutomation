from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd

# Configure WebDriver
options = Options()
options.add_argument("--headless")  # Run in background
driver = webdriver.Chrome(service=Service("path/to/chromedriver"), options=options)

def get_hotel_links(city_url, hotel_limit=100):
    hotel_links = []
    driver.get(city_url)
    sleep(5)

    while len(hotel_links) < hotel_limit:
        hotels = driver.find_elements(By.XPATH, "//a[contains(@href, '/Hotel_Review-')]")
        for hotel in hotels:
            href = hotel.get_attribute("href")
            if href and href not in hotel_links:
                hotel_links.append(href)
                if len(hotel_links) >= hotel_limit:
                    break

        try:
            next_button = driver.find_element(By.XPATH, "//a[@class='ui_button nav next primary ']")
            next_button.click()
            sleep(3)
        except:
            break

    return hotel_links

def get_reviews(hotel_url, max_reviews_per_hotel=100):
    reviews = []
    driver.get(hotel_url)
    sleep(3)

    while len(reviews) < max_reviews_per_hotel:
        review_blocks = driver.find_elements(By.XPATH, "//q[contains(@class, 'review-text')]")
        for review in review_blocks:
            text = review.text
            if text and text not in reviews:
                reviews.append(text)
                if len(reviews) >= max_reviews_per_hotel:
                    break

        try:
            next_review_btn = driver.find_element(By.XPATH, "//a[@class='ui_button nav next primary ']")
            next_review_btn.click()
            sleep(2)
        except:
            break

    return reviews

# MAIN
city_url = "https://www.tripadvisor.com/Hotels-g295424-Dubai_Emirate_of_Dubai-Hotels.html"
hotel_urls = get_hotel_links(city_url, hotel_limit=100)

data = []
for i, url in enumerate(hotel_urls):
    print(f"Scraping Hotel {i+1}: {url}")
    reviews = get_reviews(url, max_reviews_per_hotel=50)
    for r in reviews:
        data.append({'Hotel URL': url, 'Review': r})
    sleep(1)

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("tripadvisor_reviews.csv", index=False)

print(f"Total reviews collected: {len(df)}")

driver.quit()
