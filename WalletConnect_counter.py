import requests
import html
import json

#Function to retrieve the API request response in text format
def get_data (url):
    data= requests.get(url)
    data = html.unescape(data.text)
    data = json.loads(data)
    data = data['results']
    return data

#Function to extract and count the number of WalletConnect transactions 
def transactions_number(data): 
    origin= []
    counter = 0
    size = len(data)
    
    for i in range(size):
        origin.append(json.loads(data[i]['origin']))
        origin = list(filter(None, origin))
    
    size = len(origin)
    
    for i in range(size): 
        if origin[i]['name'] == "WalletConnect":
            counter = counter + 1
    print("number of WalletConnect transactions: %2f" % counter)
    return counter


if __name__ == "__main__":
    url = "https://safe-transaction-mainnet.safe.global/api/v1/safes/0xBbA4C8eB57DF16c4CfAbe4e9A3Ab697A3e0C65D8/multisig-transactions/"
    data = get_data(url)
    transactions_number(data)
