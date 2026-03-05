import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('NEWSAPI_API_KEY')
url = 'https://newsapi.org/v2/everything'

response = requests.get(url = url , 
                        params = {
                            'apiKey' : api_key ,
                            'q' :'geopolics OR "international relations"' ,
                            'from' : '2026-02-26' ,
                            'language' : 'en'}
                        ) 

if response.status_code:
    
    data = response.json()
    data_news = data['articles']


