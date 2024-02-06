from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import BaseWebDriver

class Button:
  _css_selector: str
  _driver: BaseWebDriver
  def __init__(self, css_selector: str, driver: BaseWebDriver):
    self._css_selector = css_selector
    self._driver = driver

  def is_displayed(self)-> bool:
    return self.find_button() is not None

  def click(self)-> None:
    button = self.find_button()
    button.click()

  def find_button(self)-> WebElement:
    try:
      return self._driver.find_element(By.CSS_SELECTOR, self._css_selector)
    except NoSuchElementException:
      return None

