import requests

BASE_URL = 'http://127.0.0.1:5000'

def add_message(message):
    endpoint = f'{BASE_URL}/add_message'
    data = {'message': message}
    response = requests.post(endpoint, json=data)
    return response.json()

def search_message(keyword):
    endpoint = f'{BASE_URL}/search_message'
    params = {'keyword': keyword}
    response = requests.get(endpoint, params=params)
    return response.json()

# add_message_response = add_message("enter your message")
# print("Add Message Response:", add_message_response)

# search_message_response = search_message("keyword")
# print("Search Message Response:", search_message_response)