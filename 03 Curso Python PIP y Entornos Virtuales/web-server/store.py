import requests

def get_categories():
    
    r = requests.get('https://api.escuelajs.co/api/v1/categories', verify=False)

    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    print(categories)
    # for category in categories:
    #     print(category['id'])