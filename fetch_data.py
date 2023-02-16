import requests
API_URL = "https://www.jwst.nasa.gov/content/webbLaunch/flightCurrentState2.0.json"
return requests.get(API_URL).json()['currentState']