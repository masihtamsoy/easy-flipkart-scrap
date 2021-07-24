from bs4 import BeautifulSoup
import pandas as pd
import unicodedata
from functools import partial
from selenium import webdriver
import sys
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from scrap_core import Flipkart



def prepare_info(dirtyStr):
  s = unicodedata.normalize('NFKD', dirtyStr).encode('ascii', 'ignore')
  return s.decode("utf-8")


def my_end_node(arr, tag):
   # print ("/////////////////", tag)   
   # @TODO How to pass different array flog: personal, seller
   arr.append(prepare_info(tag.text))
   return True



SELLER_INFO = {
  'pid': [],
  'seller': [],
  'sp': [],
  'cp': [],
  'dis': [],
  'deliver': []
}

def extract_seller_new():
  
  MODE='seller'
  #hello
  flipkart = Flipkart(MODE)
  flipkart.driver_initiate()

  result = flipkart.get_unique_values_from_file()
  chunks_range = flipkart.segregate_data_into_chunks()

  print (chunks_range)
  # print (result)
  pids = result[0]
  links = result[1]

  for p in range(1, len(chunks_range)):
    start = chunks_range[p][0]
    end = chunks_range[p][1]
    
    df = pd.DataFrame(SELLER_INFO)
    for i in range(start, end):
      if type(links[i]) == str:
        url = "https://www.flipkart.com" + links[i]
        print ("**URL ----> ", url)

        soup = flipkart.driver_page_soup(url)
        jsElem = flipkart.driver_js_elem()

        deliver = ""
        sp = ""
        cp = ""
        dis = ""

        for elem in jsElem:
          try:
            seller = elem.find_element_by_class_name('isp3v_').text
            # @TODO: change logic
            sp = elem.find_element_by_class_name('_30jeq3').text if elem.find_element_by_class_name('_30jeq3') else ''
            cp = elem.find_element_by_class_name('_3I9_wc').text if elem.find_element_by_class_name('_3I9_wc') else ''
            dis = elem.find_element_by_class_name('_3Ay6Sb').text if elem.find_element_by_class_name('_3Ay6Sb') else ''
            deliver = elem.find_element_by_class_name('_3XINqE').text if elem.find_element_by_class_name('_3XINqE') else ''

          except:
            pass

          # print (pids[i], prepare_info(seller), prepare_info(price), deliver)
          
          df.loc[len(df.index)] = [
            pids[i],
            seller,
            flipkart.prepare_info(sp),
            flipkart.prepare_info(cp),
            flipkart.prepare_info(dis),
            flipkart.prepare_info(deliver),
          ]

    file_name = 'seller' + str(p+1) + '.csv'
    df.to_csv(file_name, index=False, encoding='utf-8')
      




def extract_seller():

  # Intializing driver
  driver = webdriver.Chrome(executable_path = './bin/chromedriver 2')

  pids=[]
  seller_links = []
  data = pd.read_csv("./unique_pro_details.csv")

  for index, row in data.iterrows():
    # row[0] for pid
    # row[2] for link
    pids.append(row['pid'])
    seller_links.append(row['more_seller_link'])

  # print (seller_links)

  productInfo = {
    'pid': [],
    'seller': [],
    'sp': [],
    'cp': [],
    'dis': [],
    'deliver': []
  }

  df = pd.DataFrame(productInfo)

  for i in range(len(seller_links)):
    if type(seller_links[i]) == str:
      url = "https://www.flipkart.com" + seller_links[i]
      print ("**URL ----> ", url)

      # page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
      # soup = BeautifulSoup(page.text, 'html.parser')
      driver.execute_script("window.open('about:blank', 'secondtab');")
      driver.switch_to.window("secondtab")
      driver.get(url)
      
      try:
        jsElem = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME , "_2Y3EWJ")))
        print ("Page is ready!")
      except TimeoutException:
        print ("Loading took too much time!")

      deliver = ""
      sp = ""
      cp = ""
      dis = ""
      # import pdb;pdb.set_trace()
      for elem in jsElem:
        try:
          seller = elem.find_element_by_class_name('isp3v_').text
          # @TODO: change logic
          sp = elem.find_element_by_class_name('_30jeq3').text if elem.find_element_by_class_name('_30jeq3') else ''
          cp = elem.find_element_by_class_name('_3I9_wc').text if elem.find_element_by_class_name('_3I9_wc') else ''
          dis = elem.find_element_by_class_name('_3Ay6Sb').text if elem.find_element_by_class_name('_3Ay6Sb') else ''
          deliver = elem.find_element_by_class_name('_3XINqE').text if elem.find_element_by_class_name('_3XINqE') else ''

        except:
          pass

        # print (pids[i], prepare_info(seller), prepare_info(price), deliver)
        
        df.loc[len(df.index)] = [
          pids[i],
          seller,
          prepare_info(sp),
          prepare_info(cp),
          prepare_info(dis),
          prepare_info(deliver),
        ]
    

  df.to_csv('unique_seller.csv', index=False, encoding='utf-8')


def data_sanetize():
  data = pd.read_csv("./unique_seller.csv")
  for index, row in data.iterrows():
    price = row['price'].split("%")[0]
  
  # prices = [row['price'].split("%")[0] for index, row in data.iterrows()]

  # d = [0]*20
  # for price in prices:
  #   print (price)
  #   d[len(price)] += 1
  
  # print (d)
  # import pdb;pdb.set_trace()
  # # for index, row in data.iterrows():

# data_sanetize()
extract_seller_new()