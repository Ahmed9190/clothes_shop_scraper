from src.scrapers.product_scraper import ProductScraper
from src.scraping_elements.load_more_button import LoadMoreButton
from src.scrapers.clothes_scraper import ClothesScraper


class HMScraper(ClothesScraper):
  _load_more_button: LoadMoreButton
  def __init__(self, url, product_scraper: ProductScraper, load_more_button: LoadMoreButton):
    super().__init__(url, product_scraper)
    self._load_more_button = load_more_button

  async def scrape_products_and_save_to_csv(self, file_name: str):
    self._load_more_button.click_until_disappeared()

    products_count = self._product_scraper.get_product_count()

    self._load_more_button.wait_until_all_loaded(
      all_loaded_indicator_text=f"showing {products_count} of {products_count} items"
    )

    products = await self._product_scraper.scrape_all_products()
    self._product_scraper.save_to_csv(products, file_name)
