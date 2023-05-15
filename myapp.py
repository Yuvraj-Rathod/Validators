import requests
import json

URL = ""

# def get_data(id = None):
#     data = {}
#     if data is not None:
#         data = {'id': id}
#         json_data = json.dumps(data)
#         r = requests.get(url=URL, data = json_data)
#         data = r.json()
#         print(data)
#         # get_data()

def post_data():
    data = {
        'name' : 'Ravi',
        'roll' : 104 ,
        'city' : 'Mumbai'
    } 

    json_data = json.dumps(data)
    r = requests.post(url = URL,data = json_data)
    data = r.json()
    print(data)

