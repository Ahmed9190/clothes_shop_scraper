import asyncio
from typing import Callable
from selenium.webdriver.remote.webdriver import BaseWebDriver
from selenium.webdriver.common.by import By
import pandas as pd
from src.entities.product import Product

class ProductScraper:
  _image_css_selector_builder: Callable[[int], str]
  _name_css_selector_builder: Callable[[int], str]
  _price_css_selector_builder: Callable[[int], str]
  _count_css_selector: str
  _all_products_loaded_indicator_css_selector: str
  _all_products_loaded_indication_text: str
  _driver: BaseWebDriver

  def __init__(
    self,
    image_css_selector_builder: Callable[[int], str],
    name_css_selector_builder: Callable[[int], str],
    price_css_selector_builder: Callable[[int], str],
    count_css_selector: str,
    driver: BaseWebDriver
  ):
    self._image_css_selector_builder = image_css_selector_builder
    self._name_css_selector_builder = name_css_selector_builder
    self._price_css_selector_builder = price_css_selector_builder
    self._count_css_selector = count_css_selector
    self._driver = driver

  async def scrape_all_products(self)-> list[Product]:
    async_products = []
    product_count = self.get_product_count()
    for i in range(1, product_count):
      product = self.scrape_product(i)
      async_products.append(product)

    products = await asyncio.gather(*async_products)
    return products

  def get_product_count(self) -> int:
    pass

  async def scrape_product(self, product_index: int)-> Product:
    image_css_selector = self._image_css_selector_builder(product_index)
    name_css_selector = self._name_css_selector_builder(product_index)
    price_css_selector = self._price_css_selector_builder(product_index)

    image = self._driver.find_element(By.CSS_SELECTOR, image_css_selector)
    name = self._driver.find_element(By.CSS_SELECTOR, name_css_selector)
    price = self._driver.find_element(By.CSS_SELECTOR, price_css_selector)

    return Product(name.text, price.text, image.get_attribute('src'))

  def to_data_frame(self, products: list[Product])-> pd.DataFrame:
    return  pd.DataFrame(self.to_dictionary_list(products))

  def to_dictionary_list(self, products: list[Product])-> list[dict]:
    return [product.to_dict() for product in products]

  def save_to_csv(self, products: list[Product], file_name: str):
    data_frame = self.to_data_frame(products)
    data_frame.to_csv(file_name, index=False)
