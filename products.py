from scrap_core import Flipkart
import urllib.parse
import pandas as pd

PRO_INFO = {
  'pid': [],
  'name': [],
  'link': [],
}

def get_product_listing():
  flipkart = Flipkart()
  PAGE_NUM = input("Enter page number:")
  flipkart.set_pages(PAGE_NUM)

  # @HARDCODE: for URL mention page in query
  # https://www.flipkart.com/books/~cs-fw4wq89iws/pr?sid=bks&collection-tab-name=Top+JEE+Exam+Books&hpid=8lrhlQscsveO1YjEVCnSxw%3D%3D&fm=neo%2Fmerchandising&iid=M_90ecb157-3426-4b99-9350-4d9a3ab4ffa3_1.W591WTTZDWNT&ppt=clp&ppn=the-exam-store&ssid=itr2vyi9ecoqz5ds1626841885243&otracker=dynamic_omu_infinite_Exam%2BPreparation%2B_1_1.dealCard.OMU_INFINITE_W591WTTZDWNT&cid=W591WTTZDWNT&page=
  OPEN_URL = input("Enter URL:")

  # Initialize required list
  pids = []
  names = []
  detail_links = []

  # all links: with page query attached
  urls = flipkart.get_value_based_on_pages(OPEN_URL)

  flipkart.driver_initiate()

  for u in range(len(urls)):
    url = urls[u]
    soup = flipkart.driver_page_soup(url)

    # @Input
    # allDiv = soup.select('div[data-id*="TEA"]')
    # @HARDCODE: class name may change
    allDiv = soup.find_all('div', attrs={'class': '_4ddWXP'})

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


# based on all the scraped .csv files; filter out unique pids
def get_unique_pid_mapping():
  flipkart = Flipkart()
  PAGE_NUM = input("Enter count of files (pro1, pro2...) generated:")
  flipkart.set_pages(PAGE_NUM)
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
  

get_product_listing()
get_unique_pid_mapping()
