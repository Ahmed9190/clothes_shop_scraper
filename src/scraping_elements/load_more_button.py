from selenium.webdriver.support.ui import WebDriverWait
from src.scraping_elements.button import Button
from selenium.webdriver.remote.webdriver import BaseWebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoadMoreButton(Button):
  _all_loaded_indicator_css_selector: str
  _driver: BaseWebDriver

  def __init__(
    self,
    css_selector: str,
    all_loaded_indicator_css_selector: str,
    driver: BaseWebDriver
  ):
    super().__init__(css_selector)
    self._all_loaded_indicator_css_selector = all_loaded_indicator_css_selector
    self._driver = driver

  def click_until_disappeared(self):
    while self.load_more_if_exists():
      pass

  def load_more_if_exists(self)->bool:
    if super().is_displayed():
      super().click()
      return True
    return False

  def wait_until_all_loaded(self, all_loaded_indicator_text: str):
    WebDriverWait(self._driver, 30).until(
      EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, self._all_loaded_indicator_css_selector),
        all_loaded_indicator_text
      )
    )
