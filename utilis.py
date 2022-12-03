import requests, logging

logger = logging.getLogger(__name__)

def checkToken(address):
    url = f'https://api.gopluslabs.io/api/v1/token_security/56?contract_addresses={address}'
    try:
        response = requests.get(url).json()
    except:
        logger.warning("Connection problem with go+")
        return False
    if response['message'] != 'OK':
        logger.warning("Connection problem with go+: " + response['message'])
        return False
    data = response['result'][address.lower()]
    if data.get("buy_tax") == "0" and data.get("sell_tax") == "0" and data.get('is_honeypot') == "0" and data.get("is_blacklisted") == '0':
        return True
    else:
        return False

