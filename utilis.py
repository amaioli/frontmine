import requests

def checkToken(address):
    url = f'https://api.gopluslabs.io/api/v1/token_security/56?contract_addresses={address}'
    response = requests.get(url).json()
    data = response['result'][address.lower()]
    if data.get("buy_tax") == "0" and data.get("sell_tax") == "0" and data.get('is_honeypot') == "0" and data.get("is_blacklisted") == '0':
        return True
    else:
        return False

