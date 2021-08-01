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

# some database data
db_countries = {
    'usa': {
        'territory': 42.5,
        'population': 953.7,
        'language': ['english','spanish', 'portuguese']
    },
    'canada': {
        'territory': 9.9,
        'pupulation': 37.6,
        'language': ['english', 'french']
    }
}