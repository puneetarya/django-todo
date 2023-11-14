import requests
import json


URL = "http://127.0.0.1:8000/studentapi/"

def get_person_data(id=None, URL=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(f'{id} : {data}')

def post_person_data(data, URL):

    json_data = json.dumps(data)
    r = requests.post(url = URL, data=json_data)
    response = r.json()
    print(response)

def update_person_data(data, URL):
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    response = r.json()
    print(response)

def delete_person_data(data, URL):
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    response = r.json()
    print(response)


# Get data
#get_person_data(id=1, URL=URL)
#get_person_data(URL=URL)


# Post data
data = {
    'name':'Ravi',
    'roll':3,
    'city':'jhajjar'
}

post_person_data(data=data, URL=URL)

# update data
update_data = {
    'id' : 3,
    'name':'Ravi',
    'city':'Jhajjar'
}

#update_person_data(data=update_data, URL=URL)

# delete data
delete_data = {'id':3}
#delete_person_data(delete_data, URL=URL)