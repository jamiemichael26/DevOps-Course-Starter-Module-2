import requests 

def get_token():
    f = open("todo_app\\data\\key.gitignore", "r")
    for x in f:
        if x.startswith("token"):
            token = x[-64:70]
    return token.rstrip("\n")

def get_key():
    f = open("todo_app\\data\\key.gitignore", "r")
    for x in f:
        if x.startswith("key"):
           key = x[-33:37]
    return key.rstrip("\n")

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    apikey = get_key()
    apitoken = get_token()
    url = "https://api.trello.com/1/boards/c7trSbnB/cards"

    query = {
    'key': str(apikey),
    'token': str(apitoken)
    }

    response = requests.request(
    "GET",
    url,
    params=query
    )

    return response.json()

def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    url = "https://api.trello.com/1/cards"

    apikey = get_key()
    apitoken = get_token()

    query = {
    'key': apikey,
    'token': apitoken,
    'idList': '5f5be2d2c3c4723ac911bbc9',
    'name': title
    }

    requests.request(
    "POST",
    url,
    params=query
    )

def complete_item(id):
    apikey = get_key()
    apitoken = get_token()

    url = "https://api.trello.com/1/cards/" + id

    headers = {
    "Accept": "application/json"
    }

    query = {
    'key': apikey,
    'token': apitoken,
    'idList': '5f5be2d2c3c4723ac911bbcb'
    }

    requests.request(
    "PUT",
    url,
    headers=headers,
    params=query
    )
