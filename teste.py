import requests, json

url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=4cbe57e96620e802aeaa000cee7fe00e"


response = requests.get(url)

json_data = json.loads(response.text)

print(json_data['results'])
