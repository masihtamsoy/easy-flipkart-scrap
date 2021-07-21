
# test html component
# class="_1AtVbE col-12-12" container holds important data
html = """
<div class="_1YokD2 _3Mn1Gg col-8-12" style="padding:0px 0px 0px 24px">
   </div>
   <div class="_1AtVbE col-12-12">
      <div class="aMaAEs">
         <div>
            <h1 class="yhB1nd">
               <span class="B_NuCI">
                  Robert T Kiyosaki<!-- -->&nbsp;&nbsp;(Paperback, Robert T. Kiyosaki)
               </span>
            </h1>
         </div>
         <div class="">
            <div class="_3_L3jD">
               <div class="gUuXy- _16VRIQ">
                  <span id="productRating_LSTRBKG25UHG45PP9FC00ZQUI_RBKG25UHG45PP9FC_" class="_1lRcqv">
                     <div class="_3LWZlK">4.4<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==" class="_1wB99o"></div>
                  </span>
                  <span class="_2_R_DZ"><span><span>286 Ratings&nbsp;</span><span class="_13vcmD">&amp;</span><span>&nbsp;44 Reviews</span></span></span>
               </div>
            </div>
         </div>
         <div class="dyC4hf">
            <div class="CEmiEU">
               <div class="_25b18c">
                  <div class="_30jeq3 _16Jk6d">₹120</div>
                  <div class="_3I9_wc _2p6lqe">
                     ₹<!-- -->399
                  </div>
                  <div class="_3Ay6Sb _31Dcoz"><span>69% off</span></div>
               </div>
            </div>
            <div class="_1V9q7_"><img class="_3ECE0V" src="//static-assets-web.flixcart.com/www/linchpin/fk-cp-zion/img/info-basic_6c1a38.svg" id="price-info-icon"></div>
         </div>
      </div>
   </div>
   <div class="_1AtVbE col-12-12">
      <div class="_3Z0lU8">
         <div class="rd9nIL">Available offers</div>
      </div>
      <div class="_3TT44I">
         <div class="WT_FyS">
            <div class="XUp0WS">
               <span class="_3j4Zjq row">
                  <img src="https://rukminim1.flixcart.com/www/36/36/promos/06/09/2016/c22c9fc4-0555-4460-8401-bf5c28d7ba29.png?q=90" width="18" height="18" class="_3HLfAg">
                  <li class="_16eBzU col">
                     <span class="u8dYXW">Bank Offer</span><span>5% Unlimited Cashback on Flipkart Axis Bank Credit Card</span>
                     <div class="Bv11UC _1qNw3R"><span class="fGhUR2">T&amp;C</span></div>
                  </li>
               </span>
               <span class="_3j4Zjq row">
                  <img src="https://rukminim1.flixcart.com/www/36/36/promos/06/09/2016/c22c9fc4-0555-4460-8401-bf5c28d7ba29.png?q=90" width="18" height="18" class="_3HLfAg">
                  <li class="_16eBzU col">
                     <span class="u8dYXW">Bank Offer</span><span>20% off on 1st txn with Amex Network Cards issued by ICICI Bank,IndusInd Bank,SBI Cards and Mobikwik</span>
                     <div class="Bv11UC _1qNw3R"><span class="fGhUR2">T&amp;C</span></div>
                  </li>
               </span>
               <span class="_3j4Zjq row">
                  <img src="https://rukminim1.flixcart.com/www/36/36/promos/06/09/2016/c22c9fc4-0555-4460-8401-bf5c28d7ba29.png?q=90" width="18" height="18" class="_3HLfAg">
                  <li class="_16eBzU col">
                     <span class="u8dYXW">Bank Offer</span><span>10% Off on Bank of Baroda Mastercard debit card first time transaction, Terms and Condition apply</span>
                     <div class="Bv11UC _1qNw3R"><span class="fGhUR2">T&amp;C</span></div>
                  </li>
               </span>
               <span class="_3j4Zjq row">
                  <img src="https://rukminim1.flixcart.com/www/36/36/promos/06/09/2016/c22c9fc4-0555-4460-8401-bf5c28d7ba29.png?q=90" width="18" height="18" class="_3HLfAg">
                  <li class="_16eBzU col">
                     <span class="u8dYXW">Bank Offer</span><span>10% Off on First time ICICI Mastercard Credit Card transaction, Terms and Condition apply</span>
                     <div class="Bv11UC _1qNw3R"><span class="fGhUR2">T&amp;C</span></div>
                  </li>
               </span>
            </div>
            <button class="_1JIkBw">
               <div class="row">
                  <div class="IMZJg1"><span>View 2 more offers</span></div>
               </div>
            </button>
         </div>
      </div>
   </div>
</div>
"""

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
from products import PAGE_NUM


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
   flipkart.set_pages(PAGE_NUM)
   flipkart.driver_initiate()

   productInfo = {
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
   'top_seller': [],
   'more_seller_link': [],
   }

   df = pd.DataFrame(productInfo)

   pids = []
   product_detail_links = []

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

         # import pdb;pdb.set_trace()

         try:
            
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
            prepare_info(top_seller),
            more_seller_link,
         ]
      
      file_name = 'proDetail' + str(p+1) + '.csv'
      df.to_csv(file_name, index=False, encoding='utf-8')



# From collected multiple scrapped product details; return unique pids
def get_unique_pid_mapping():
   flipkart = Flipkart()
   flipkart.set_pages(PAGE_NUM)
   # put unique data in proUnique.csv
   pids=[]

   productInfo = {
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
   'top_seller': [],
   'more_seller_link': [],
   }

   df = pd.DataFrame(productInfo)

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


# extract_product_details()
get_unique_pid_mapping()

# [@INFO] Wrong intution, there is inconsistency in order of divs
# For different product divs[3] is not same
# # @Hardcode
# # divs[3] - name, rating, review, sp, sp, dis
# # divs[7] - seller: name, rating
# divs = soup.find_all("div", {"class": "_1AtVbE col-12-12"})
# # print ("**PARENT DIVS ----> ", divs)

# for d in range(8):
# if (d in [3, 7]):
#    myArr = []
#    end_node = partial(my_end_node, myArr)
#    divs[d].find_all(end_node)

#    print ("myArr===>", pids[i], myArr)
#    df.loc[len(df.index)] = [pids[i], myArr]
