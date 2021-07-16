from scrap_core import Flipkart
import urllib.parse
import pandas as pd

flipkart = Flipkart()
flipkart.set_pages(25)

def get_product_listing():
  # Initialize required list
  pids = []
  names = []
  detail_links = []

  # all links
  urls = flipkart.get_value_based_on_pages('https://www.flipkart.com/search?q=tea&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_6_3_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_6_3_na_na_na&as-pos=6&as-type=RECENT&suggestionId=tea&requestId=5434bf64-a302-4d6b-a290-6fe47579c5bc&as-searchtext=tea&page=')

  flipkart.driver_initiate()

  for u in range(len(urls)):
    url = urls[u]
    soup = flipkart.driver_page_soup(url)

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


def get_unique_pid_mapping():
  # put unique data in proUnique.csv
  pids=[]
  product_detail_links = []

  productInfo = {
    'pid': [],
    'name': [],
    'link': [],
  }

  df = pd.DataFrame(productInfo)

  file_names = flipkart.get_value_based_on_pages('pro', ".csv")

  for file_name in file_names:
    data = pd.read_csv(file_name)

    for index, row in data.iterrows():
      # row[0] for pid
      # row[2] for link
      if row['pid'] not in pids:
        pids.append(row['pid'])
        df.loc[len(df.index)] = row

  df.to_csv('unique_pro.csv', index=False, encoding='utf-8')
  
# get_product_listing()
get_unique_pid_mapping()