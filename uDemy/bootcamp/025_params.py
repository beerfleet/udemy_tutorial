import requests

url = "https://icanhazdadjoke.com/search"
response = requests.get(
        url,  
        headers={"Accept": "application/json"}, 
        params={"term": "woman"}
)

data = response.json()
data_results = data["results"]

for joke in data_results:
    print(joke['joke'])

print(f"status: {data['status']}")
