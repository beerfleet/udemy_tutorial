import requests

def show_help():
    print(dir(requests.Request))
    #print(dir(requests.ConnectTimeout))
    print(help(requests.Request))


def make_request(url):    
    resp = requests.get(url)
    return resp
    
def print_headers(resp):
    for hd_k,hd_v in resp.headers.items():
        print(f"{hd_k}:{hd_v}")

resp = make_request("https://news.ycombinator.com")
