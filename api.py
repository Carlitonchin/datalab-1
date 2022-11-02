import requests

def get_cat_facts():
    url = "https://catfact.ninja/facts"

    response = requests.get(url).json()
    limit = response['total']
    
    response = requests.get(url + "?limit=" + str(limit)).json()

    return response['data']

