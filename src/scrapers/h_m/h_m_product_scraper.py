from src.scrapers.product_scraper import ProductScraper
from selenium.webdriver.remote.webdriver import BaseWebDriver
from selenium.webdriver.common.by import By
from typing import Callable

class HMProductScraper(ProductScraper):
  def __init__(
    self,
    image_css_selector_builder: Callable[[int], str],
    name_css_selector_builder: Callable[[int], str],
    price_css_selector_builder: Callable[[int], str],
    count_css_selector: str,
    driver: BaseWebDriver
  ):
    super().__init__(
      image_css_selector_builder,
      name_css_selector_builder,
      price_css_selector_builder,
      count_css_selector,
      driver
    )

  def get_product_count(self) -> int:
    product_count_element = super()._driver.find_element(By.CSS_SELECTOR, self._count_css_selector)
    product_count_text = product_count_element.get_attribute('innerText')
    product_count_string = product_count_text.split(" ")[0]
    product_count = int(product_count_string)
    return product_count