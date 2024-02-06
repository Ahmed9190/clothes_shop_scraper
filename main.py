import asyncio
from selenium import webdriver
from src.scrapers.h_m.h_m_product_scraper import HMProductScraper

from src.scrapers.h_m.h_m_scraper import HMScraper
from src.scraping_elements.load_more_button import LoadMoreButton

driver = webdriver.Chrome()

async def main():
  url = 'https://eg.hm.com/en/shop-men/shop-product/hoodies-sweatshirts/'
  driver.get(url)

  product_scraper = HMProductScraper(
    image_css_selector_builder = lambda i: f"#plp-hits > div > div:nth-child({i}) > article > div > a > div > div > div > img",
    name_css_selector_builder = lambda i: f"#plp-hits > div > div:nth-child({i}) > article > div > div.product-plp-detail-wrapper > h2 > a > div > span",
    price_css_selector_builder = lambda i: f"#plp-hits > div > div:nth-child({i}) > article > div > div.product-plp-detail-wrapper > div.price-block > span > div > span.price-amount",
    count_css_selector = "#alshaya-algolia-plp > div.block.block-alshaya-grid-count-block > div.total-result-count > div > div > span",
    driver=driver
  )

  load_more_button = LoadMoreButton(
    load_more_button_css_selector="#plp-hits > ul > li:nth-child(2) > button",
    all_loaded_indicator_css_selector="#plp-hits > ul > li > span",
    driver=driver
  )

  h_m_scraper = HMScraper(
    url,
    product_scraper,
    load_more_button,
  )

  await h_m_scraper.scrape_products_and_save_to_csv("src/data/products.csv")
  driver.quit()


if __name__ == "__main__":
  asyncio.run(main())