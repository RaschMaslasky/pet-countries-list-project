from fastapi import FastAPI
import requests

app = FastAPI()

# глобальная переменная
db_countries = []

class RequestAPI:
  def get_list(self):
    url = "https://restcountries.eu/rest/v2/all"
    global db_countries
    db_countries =  requests.get(url).json()	
    return db_countries

# home page
@app.get("/")
def index():
  return "Welcome! This is a home page"

# get list about countries
@app.get('/countries/list')
def get_list():
  request = RequestAPI() 
  return request.get_list() 

# get info about countries
@app.get('/countries/{name}')
def get_info(name):
  if (len(db_countries) > 0):
    search = next((item for item in db_countries if item["name"] == name), None)	
    if (search):
      result = search
    else:
      result = "Sorry. There are not any info about %s" %name
  else:
    result = "Sorry. Info about coutries reload. Please try again" 
    request = RequestAPI()
    request.get_list()

  return result