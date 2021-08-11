import requests
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.applications import Starlette

app = FastAPI()

# global variable
db_countries = []

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


class RequestAPI:
  def get_list(self):
    url = "https://restcountries.eu/rest/v2/all"
    global db_countries
    db_countries =  requests.get(url).json()	
    return db_countries

# home page
@app.route("/")
def index(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

# get list about countries
@app.get('/countries/list')
def get_list(request: Request):
  req = RequestAPI() 
  result = req.get_list()  
  return templates.TemplateResponse("colist.html", {"request": request, "countrieslist": result})

# get info about countries
@app.get('/countries/{coname}')
def get_info(request: Request, coname):
  if (len(db_countries) > 0):
    search = next((item for item in db_countries if item["name"] == coname), None)	
    if (search):
      result = templates.TemplateResponse("country.html", {"request": request, "country": search})  
    else:
      result = "Sorry, There is not any info about %s" %coname
  else:
    result = "Countries info has updated. Please refresh current page." 
    request = RequestAPI()
    request.get_list()

  return result