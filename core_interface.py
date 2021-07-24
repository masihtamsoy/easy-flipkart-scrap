from scrap_core import Flipkart
import pandas as pd


class ScraperInterface:
  def __init__(self) -> None:
    pass

  def extract_details(self, mode, info_dict):
    MODE = mode
    INFO_DICT = info_dict

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
  
      df = pd.DataFrame(INFO_DICT)
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

