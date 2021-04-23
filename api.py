import requests
#Data returns in JSON format 
import json
#Response is requested from api using link and key below
response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

# iterate through returned JSON data. Can plug in Parameters to search for inside of returned data
for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
    else:
        print("No unanswered questions")
    