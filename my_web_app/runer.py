import requests
from my_web_app.model import Example
from my_web_app.router import VALID_API_KEY

def call_here():
        
    url = "http://127.0.0.1:8000/here/tom?query=123"

    payload = Example(name="ALICE")

    response = requests.get(url, json=payload.model_dump())

    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")




def call_account(should_auth : bool):
        
    url = "http://127.0.0.1:8000/account/123"    
    headers = {
        "X-API-Key": VALID_API_KEY,
        "Content-Type": "application/json"
    }
    if should_auth:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
    else:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")


def call_transaction():
        
    url = "http://127.0.0.1:8000/transaction?account_number=003"    
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    url = "http://127.0.0.1:8000/transaction/fileter?account_number=003&transaction_type=DEBIT"    
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")




# call_account(should_auth=True)
call_transaction()

