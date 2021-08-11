import requests

class RequestAPI:
    
  def get_list(self):
    url = "https://restcountries.eu/rest/v2/all"
    result =  request.get(url).json()
    return result['content']

  def get_info(self, name):
    url = "https://restcountries.eu/rest/v2/name/"+name
    result =  request.get(url).json()
    return result['content']	    
}