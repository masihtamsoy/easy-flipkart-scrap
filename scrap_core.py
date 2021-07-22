from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
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
  
  def driver_js_elem(self, attr = {'class': "_2Y3EWJ"}):
    try:
      jsElem = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME , attr['class'])))
      print ("Page is ready!")
    except TimeoutException:
      print ("Loading took too much time!")
    
    return jsElem

  # Use for getting file_names + urls based on pages count
  def get_value_based_on_pages(self, prefix="", suffix=""):
    values = []
    pages = self.pages + 1
    for i in range(1, pages):
      file_name = prefix + str(i) + suffix
      values.append(file_name)
    return values

  def get_values_from_file(self, file_name):
    pids = []
    links = []

    data = pd.read_csv(file_name)
    for index, row in data.iterrows():
      # row[0] for pid
      # row[2] for link
      if row['pid'] not in pids:
        pids.append(row['pid'])
        links.append(row['link'])
    
    return [pids, links]