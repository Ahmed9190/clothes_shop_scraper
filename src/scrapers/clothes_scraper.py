
from src.scrapers.product_scraper import ProductScraper


class ClothesScraper:
  _url: str
  _product_scraper: ProductScraper
  def __init__(self, url, product_scraper: ProductScraper):
    self._url = url
    self._product_scraper = product_scraper

  async def scrape_products_and_save_to_csv(self, file_name: str):
    pass