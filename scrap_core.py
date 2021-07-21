from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import urllib.parse
import unicodedata


class Flipkart:
  def __init__(self):
    self.base_url = "https://www.flipkart.com"
  
  def set_pages(self, pages):
    self.pages = int(pages)
  
  def prepare_info(self, dirtyStr):
    s = unicodedata.normalize('NFKD', dirtyStr).encode('ascii', 'ignore')
    return s.decode("utf-8")

  def driver_initiate(self):
    # Intializing driver
    self.driver = webdriver.Chrome(executable_path = './bin/chromedriver 2')
    
  def driver_page_soup(self, url):
    self.driver.execute_script("window.open('about:blank', 'secondtab');")
    self.driver.switch_to.window("secondtab")
    self.driver.get(url)

    content = self.driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    return soup
  
  # Use for getting file_names + urls based on pages count
  def get_value_based_on_pages(self, prefix="", suffix=""):
    values = []
    pages = self.pages + 1
    for i in range(1, pages):
      file_name = prefix + str(i) + suffix
      values.append(file_name)
    return values
