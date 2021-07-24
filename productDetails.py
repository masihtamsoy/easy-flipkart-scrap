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


def extract_product_details():
   MODE='pd'
   #hello
   flipkart = Flipkart(MODE)
   flipkart.driver_initiate()

   result = flipkart.get_unique_values_from_file()
   chunks_range = flipkart.segregate_data_into_chunks()

   print (chunks_range)
   # print (result)
   pids = result[0]
   links = result[1]

   for p in range(0, len(chunks_range)):
      start = chunks_range[p][0]
      end = chunks_range[p][1]
      
      df = pd.DataFrame(PRODUCT_INFO)
      for i in range(start, end):
         url = flipkart.base_url + links[i]
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
            flipkart.prepare_info(name),
            flipkart.prepare_info(rate_score),
            flipkart.prepare_info(rating_review),
            flipkart.prepare_info(sp),
            flipkart.prepare_info(cp),
            flipkart.prepare_info(dis),
            wt_label,
            qty,
            highlight,
            inventory_alert,
            stock_alert,
            flipkart.prepare_info(top_seller),
            more_seller_link,
         ]
      
      file_name = 'proDetail' + str(p+1) + '.csv'
      df.to_csv(file_name, index=False, encoding='utf-8')



def get_unique_pid_mapping():
   flipkart = Flipkart("pd")
   flipkart.merge_multiple_sources_into_master(PRODUCT_INFO)

extract_product_details()
get_unique_pid_mapping()
