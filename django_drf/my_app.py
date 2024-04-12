import requests

import json


# url="http://127.0.0.1:8000/student_detail/2"
URL="http://127.0.0.1:8000/student_api/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)
# get_data()
def create_data():

    data={
        "name":"Rarfaraz",
        "roll":30,
        "city":"delhi"

    }

    # r=requests.get(url=url)
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)
# create_data()
def update_data():
    data={
        "id":6,
        "name":"uvais",
        "roll":100,
        "city":"moradabad"

    }
   
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)
# update_data()
def delete_data():
    data={
        "id":6,

    }
   
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)
# delete_data()