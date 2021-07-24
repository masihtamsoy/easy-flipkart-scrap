import pandas as pd
from scrap_core import Flipkart


SELLER_INFO = {
  'pid': [],
  'seller': [],
  'sp': [],
  'cp': [],
  'dis': [],
  'deliver': []
}

def extract_seller():
  
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

  for p in range(0, len(chunks_range)):
    start = chunks_range[p][0]
    end = chunks_range[p][1]
    
    df = pd.DataFrame(SELLER_INFO)
    for i in range(start, end):
      if type(links[i]) == str:
        url = flipkart.base_url + links[i]
        print ("**URL ----> ", url)

        soup = flipkart.driver_page_soup(url)
        jsElem = flipkart.driver_js_elem()

        deliver = ""
        sp = ""
        cp = ""
        dis = ""

        for elem in jsElem:
          try:
            # @HARDCODE
            seller = elem.find_element_by_class_name('isp3v_').text
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


def get_unique():
  flipkart = Flipkart("seller")
  flipkart.merge_multiple_sources_into_master(SELLER_INFO)


extract_seller()
get_unique()
