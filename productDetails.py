import sys
from os import access
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import unicodedata
from functools import partial
from scrap_core import Flipkart
import math


PRODUCT_INFO = {
   'pid': [],
   'name': [],
   'rate_score': [],
   'rating_review': [],
   'sp': [],
   'cp': [],
   'dis': [],
   'wt_label': [],
   'qty': [],
   'highlight': [],
   'inventory_alert': [],
   'stock_alert': [],
   'top_seller': [],
   'more_seller_link': [],
   }

def prepare_info(dirtyStr):
  s = unicodedata.normalize('NFKD', dirtyStr).encode('ascii', 'ignore')
  return s.decode("utf-8")


def my_end_node(arr, tag):
   # print ("/////////////////", tag)   
   # @TODO How to pass different array flog: personal, seller
   arr.append(prepare_info(tag.text))
   return True

def extract_product_details():
   flipkart = Flipkart()
   flipkart.driver_initiate()

   pids = []
   product_detail_links = []

   df = pd.DataFrame(PRODUCT_INFO)
   data = pd.read_csv('unique_pro.csv')

   for index, row in data.iterrows():
      # row[0] for pid
      # row[2] for link
      if row['pid'] not in pids:
         pids.append(row['pid'])
         product_detail_links.append(row['link'])

   # import pdb;pdb.set_trace()
   chunk = 50
   x = math.ceil(len(data)/chunk)

   # @NOTE: in each iteration chunks size requirest are being made
   for p in range(0, x):
      start = p*chunk
      end = start + chunk
      if end > len(product_detail_links):
         end = len(product_detail_links)
      
      print ("start end", start, end)
      for i in range(start, end):
         url = "https://www.flipkart.com" + product_detail_links[i]
         # test url
         # url = "https://www.flipkart.com/octavius-premium-assam-kadak-ctc-chai-tea-pouch/p/itmfeswawz4byagf?pid=TEAFERZCFGGT2PNH&lid=LSTTEAFERZCFGGT2PNHXK10XB&marketplace=FLIPKART&q=tea&store=eat%2Ffpm&srno=s_7_255&otracker=AS_Query_OrganicAutoSuggest_6_3_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_6_3_na_na_na&fm=organic&iid=1722fccc-4461-4e9b-afb9-f8bf01b2935c.TEAFERZCFGGT2PNH.SEARCH&ppt=sp&ppn=sp&ssid=r8ukfaozcw0000001626416478633&qH=7239ea2b5dc943f6"
         print ("**URL ----> ", url)

         soup = flipkart.driver_page_soup(url)

         more_seller_link = ""
         qty = []
         highlight = []
         wt_label = []
         stock_alert = ""
         inventory_alert = ""

         # import pdb;pdb.set_trace()

         try:
            # @HARDCODE: List of all hardcode attrs
            name = soup.find('span', attrs={'class': "B_NuCI"}).text
            rate_score = soup.find('div', attrs={'class': "_3LWZlK"}).text if soup.find('div', attrs={'class': "_3LWZlK"}) else ''
            rating_review = soup.find('span', attrs={'class': "_2_R_DZ"}).text if soup.find('span', attrs={'class': "_2_R_DZ"}) else ''
            sp = soup.find('div', attrs={'class': "_30jeq3"}).text if soup.find('div', attrs={'class': "_30jeq3"}) else ''
            cp = soup.find('div', attrs={'class': "_3I9_wc"}).text if soup.find('div', attrs={'class': "_3I9_wc"}) else ''
            dis = soup.find('div', attrs={'class': "_3Ay6Sb"}).text if soup.find('div', attrs={'class': "_3Ay6Sb"}) else ''
            wt_label = soup.find('div', attrs={'class': "V_omJD"}).text if soup.find('div', attrs={'class': "V_omJD"}) else ''
            qty = [ x.text for x in soup.find('ul', attrs={'class': "_1q8vHb"}).findAll('li') ] if soup.find('ul', attrs={'class': "_1q8vHb"}) else ''
            highlight = [ x.text for x in soup.find('ul', attrs={'class': "_2418kt"}).findAll('li') ] if soup.find('ul', attrs={'class': "_2418kt"}) else ''
            top_seller = soup.find('div', attrs={'id': "sellerName"}).text if soup.find('div', attrs={'id': "sellerName"}) else ''
            more_seller_link = soup.find('li', attrs={'class': "_38I6QT"}).find('a').get('href') if soup.find('li', attrs={'class': "_38I6QT"}) else ''
            stock_alert = soup.find('div', attrs={'class': "_16FRp0"}).text if soup.find('div', attrs={'class': "_16FRp0"}) else ''
            inventory_alert = soup.find('div', attrs={'class': "_2JC05C"}).text if soup.find('div', attrs={'class': "_2JC05C"}) else ''
            
         except AttributeError:
            print("invalid div class")
            pass
         except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

         df.loc[len(df.index)] = [
            pids[i],
            prepare_info(name),
            prepare_info(rate_score),
            prepare_info(rating_review),
            prepare_info(sp),
            prepare_info(cp),
            prepare_info(dis),
            wt_label,
            qty,
            highlight,
            inventory_alert,
            stock_alert,
            prepare_info(top_seller),
            more_seller_link,
         ]
      
      file_name = 'proDetail' + str(p+1) + '.csv'
      df.to_csv(file_name, index=False, encoding='utf-8')



# From collected multiple scrapped product details; return unique pids
def get_unique_pid_mapping():
   flipkart = Flipkart()
   PAGE_NUM = input("Enter count of files (proDetail1, proDetail2...) generated:")
   flipkart.set_pages(PAGE_NUM)

   # put unique data in proUnique.csv
   pids=[]

   df = pd.DataFrame(PRODUCT_INFO)

   file_names = flipkart.get_value_based_on_pages('proDetail', ".csv")

   for file_name in file_names:
      data = pd.read_csv(file_name)

      for index, row in data.iterrows():
         # row[0] for pid
         # row[2] for link
         if row['pid'] not in pids:
            pids.append(row['pid'])
            df.loc[len(df.index)] = row

   df.to_csv('unique_pro_details.csv', index=False, encoding='utf-8')


extract_product_details()
get_unique_pid_mapping()
