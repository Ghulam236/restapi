import requests

import json


# url="http://127.0.0.1:8000/student_detail/2"
URL="http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    headers = {
    "Content-Type": "application/json"  # Set the content type to JSON
   }
    json_data=json.dumps(data)
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# get_data()
def create_data():

    data={
        "name":"Shoaib",
        "empid":10,
        "designation":"backend engenner"

    }

    # r=requests.get(url=url)
    # ######## if i want parsed data print in views then i use these lines 
#     headers = {
#     "Content-Type": "application/json"  # Set the content type to JSON
#    }
    headerss={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headerss,data=json_data) 
    # json_data=json.dumps(data)
    # r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)
# create_data()
def update_data():
    data={
        "id":3,
        "name":"Uvais",
        "empid":12,
        "designation":"software Engeener"


    }
    headers = {
    "Content-Type": "application/json"  # Set the content type to JSON
   }
   
    json_data=json.dumps(data)
    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# update_data()
def delete_data():
    data={
        "id":3,

    }
    headers = {
    "Content-Type": "application/json"  # Set the content type to JSON
   }
   
    json_data=json.dumps(data)
    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
delete_data()