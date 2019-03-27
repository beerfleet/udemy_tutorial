import requests
    
def get_joke(term = ""):
    if term:
        url = f"https://icanhazdadjoke.com/search?term={term}"
    else:
        url = "https://icanhazdadjoke.com/"
    hdrs = {"Accept": "application/json"}
    # hdrs = {"Accept": "text/plain"}
    resp = requests.get(url,  headers=hdrs)
    return resp
    
resp = get_joke("lad")

#help(resp)
print(type(resp.text))
print(type(resp.json()))
print(resp.text)

json_resp = resp.json()
jokes_list = json_resp["results"]
for joke in jokes_list:
   print(joke['joke'])
