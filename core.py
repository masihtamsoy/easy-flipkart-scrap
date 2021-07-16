
# test html component
html = """
<div>
  <div data-id="TEAETC92QASWGFTV" style="width: 25%;">
   <div class="_4ddWXP" data-tkid="96625525-76a4-4915-9f75-5191f782db14.TEAETC92QASWGFTV.SEARCH">
      <a class="_2rpwqI" target="_blank" rel="noopener noreferrer" href="/red-label-tea-box/p/itmewyzfkfza9fyx?pid=TEAETC92QASWGFTV&amp;lid=LSTTEAETC92QASWGFTVCAQTUY&amp;marketplace=GROCERY&amp;q=tea&amp;store=eat%2Ffpm&amp;srno=s_1_14&amp;otracker=AS_Query_OrganicAutoSuggest_5_3_na_na_na&amp;otracker1=AS_Query_OrganicAutoSuggest_5_3_na_na_na&amp;fm=SEARCH&amp;iid=96625525-76a4-4915-9f75-5191f782db14.TEAETC92QASWGFTV.SEARCH&amp;ppt=sp&amp;ppn=sp&amp;qH=7239ea2b5dc943f6">
         <div>
            <div>
               <div class="CXW8mj _21_khk" style="height: 230px; width: 230px;"><img class="_396cs4 _3exPp9" alt="Red Label Tea Box" src="https://rukminim1.flixcart.com/image/612/612/jq4353k0/tea/f/t/v/250-na-regular-tea-red-label-leaves-original-imafc7agtzrawhhw.jpeg?q=70"></div>
            </div>
         </div>
         <div class="_2hVSre _1eAP-x">
            <div class="_36FSn5">
               <svg xmlns="http://www.w3.org/2000/svg" class="_1l0elc" width="16" height="16" viewBox="0 0 20 16">
                  <path d="M8.695 16.682C4.06 12.382 1 9.536 1 6.065 1 3.219 3.178 1 5.95 1c1.566 0 3.069.746 4.05 1.915C10.981 1.745 12.484 1 14.05 1 16.822 1 19 3.22 19 6.065c0 3.471-3.06 6.316-7.695 10.617L10 17.897l-1.305-1.215z" fill="#2874F0" class="eX72wL" stroke="#FFF" fill-rule="evenodd" opacity=".9"></path>
               </svg>
            </div>
         </div>
      </a>
      <a class="s1Q9rs" title="Red Label Tea Box" target="_blank" rel="noopener noreferrer" href="/red-label-tea-box/p/itmewyzfkfza9fyx?pid=TEAETC92QASWGFTV&amp;lid=LSTTEAETC92QASWGFTVCAQTUY&amp;marketplace=GROCERY&amp;q=tea&amp;store=eat%2Ffpm&amp;srno=s_1_14&amp;otracker=AS_Query_OrganicAutoSuggest_5_3_na_na_na&amp;otracker1=AS_Query_OrganicAutoSuggest_5_3_na_na_na&amp;fm=SEARCH&amp;iid=96625525-76a4-4915-9f75-5191f782db14.TEAETC92QASWGFTV.SEARCH&amp;ppt=sp&amp;ppn=sp&amp;qH=7239ea2b5dc943f6">Red Label Tea Box</a>
      <div class="_3Djpdu">250 g</div>
      <div class="gUuXy- _2D5lwg">
         <span id="productRating_LSTTEAETC92QASWGFTVCAQTUY_TEAETC92QASWGFTV_" class="_1lRcqv">
            <div class="_3LWZlK">4.4<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==" class="_1wB99o"></div>
         </span>
         <span class="_2_R_DZ">(13,017)</span>
      </div>
      <a class="_8VNy32" target="_blank" rel="noopener noreferrer" href="/red-label-tea-box/p/itmewyzfkfza9fyx?pid=TEAETC92QASWGFTV&amp;lid=LSTTEAETC92QASWGFTVCAQTUY&amp;marketplace=GROCERY&amp;q=tea&amp;store=eat%2Ffpm&amp;srno=s_1_14&amp;otracker=AS_Query_OrganicAutoSuggest_5_3_na_na_na&amp;otracker1=AS_Query_OrganicAutoSuggest_5_3_na_na_na&amp;fm=SEARCH&amp;iid=96625525-76a4-4915-9f75-5191f782db14.TEAETC92QASWGFTV.SEARCH&amp;ppt=sp&amp;ppn=sp&amp;qH=7239ea2b5dc943f6">
         <div class="_25b18c">
            <div class="_30jeq3">₹130</div>
         </div>
      </a>
      <div><img id="supermart-logoTEAETC92QASWGFTV" class="_3K1taq" src="//static-assets-web.flixcart.com/www/linchpin/fk-cp-zion/img/grocery-logo-green_7fba49.svg"></div>
      <div class="_2ZdXDB">
         <div class="_3xFhiH">
            <div class="_2Tpdn3 _18hQoS" style="color: rgb(38, 165, 65); font-size: 12px; font-style: normal; font-weight: 400;">Buy ₹3000 more, save extra ₹200</div>
         </div>
      </div>
   </div>
  </div>
<div>
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import urllib.parse

# Intializing driver
driver = webdriver.Chrome(executable_path = './bin/chromedriver 2')

# Initialize required list
pids = []
names = []
detail_links = []

urls = []
# 25 pages for tea
for i in range(1, 26):
   url = 'https://www.flipkart.com/search?q=tea&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_6_3_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_6_3_na_na_na&as-pos=6&as-type=RECENT&suggestionId=tea&requestId=5434bf64-a302-4d6b-a290-6fe47579c5bc&as-searchtext=tea&page=' + str(i)
   urls.append(url)


# print (urls)

for u in range(len(urls)):
   # @Input
   # URL to fetch from Can be looped over / crawled multiple urls
   # driver.get(urls[u])

   url = urls[u]
   driver.execute_script("window.open('about:blank', 'secondtab');")
   driver.switch_to.window("secondtab")
   driver.get(url)

   content = driver.page_source
   soup = BeautifulSoup(content)

   # @Input
   allDiv = soup.select('div[data-id*="TEA"]')

   for d in range(len(allDiv)):
      div = allDiv[d]
      allA = div.findAll('a',href=True)
      
      # @Hardcode [1]
      name = allA[1].text
      names.append(name)
      link = allA[1].get('href')
      detail_links.append(link)
      
      query = urllib.parse.parse_qs(urllib.parse.urlparse(link).query)
      pid = query['pid']
      pids += pid


   file_name = 'pro'+ str(u+1) + '.csv'
   print("file_name", file_name)
   df = pd.DataFrame({'pid': pids,'name':names, 'link': detail_links})
   df.to_csv(file_name, index=False, encoding='utf-8')

