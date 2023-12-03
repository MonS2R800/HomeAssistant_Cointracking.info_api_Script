import requests
import time
import hashlib
import hmac
import json

# Replace “your_api_key” and “your_api_secret” with your actual credentials
api_key = 'your_api_key'
api_secret = 'your_api_secret'


def KAPI_Private(api_key, api_secret):
    # Replace 'getBalance' with the actual balance method
    parameters = 'getBalance'

    api_nonce = str(int(time.time() * 1000))
    api_post = f'method={parameters}&nonce={api_nonce}'

    api_hmac = hmac.new(api_secret.encode('utf-8'), api_post.encode('utf-8'), hashlib.sha512)
    api_signature = api_hmac.hexdigest()

    headers = {
        'Key': api_key,
        'Sign': api_signature
    }

    payload = {
        'method': parameters,
        'nonce': api_nonce
    }
    try:
        response = requests.post('https://cointracking.info/api/v1/', headers=headers, data=payload)
        api_data = response.text

        # Optional: Process the data according to your requirements
        print(api_data)

        # Extract specific values ​​from the JSON
        data_dict = json.loads(api_data)

        success = data_dict.get('success')
        method = data_dict.get('method')
        account_currency = data_dict.get('account_currency')

        print(f"Success: {success}, Method: {method}, Account Currency: {account_currency}")

        # Access details (example: account_summary)
        account_summary = data_dict.get('summary', {}).get('value_fiat')
        # ada_summary = data_dict.get('details', {}).get('ADA', {}).get('value_fiat')
        # matic_summary = data_dict.get('details', {}).get('MATIC', {}).get('value_fiat')
        # vet_summary = data_dict.get('details', {}).get('VET', {}).get('value_fiat')
        # eth_summary = data_dict.get('details', {}).get('ETH', {}).get('value_fiat')

        print(f"account_summary: {account_summary:.8}"),
        #print(f"ADA Balance: {ada_summary:.7}"),
        #print(f"MATIC Balance: {matic_summary:.7}"),
        #print(f"VET Balance: {vet_summary:.7}"),
        #print(f"ETH Balance: {eth_summary:.7}"),
        
        return api_data
    except Exception as e:
        print(f'Fehler beim Abrufen der Daten: {str(e)}')

# Example call to the function
result = KAPI_Private(api_key, api_secret)