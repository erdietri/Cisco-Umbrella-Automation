# Prints all Umbrella activity (dns/proxy/firewall/intrusion) from the past 7 days to now
import requests, os
from dotenv import load_dotenv 

# This script is written under the assumption that it will be run on a weekly basis.
# Access token generation also requires that the user has a valid Umbrella API Key and Secret: https://developer.cisco.com/docs/cloud-security/#!authentication/manage-api-keys

load_dotenv()

# Environmental variables should contain your org's values in .env file.

client_key = os.environ['API_KEY']
client_secret = os.environ['KEY_SECRET']

# Relevant v2 Umbrella API endpoints
base_url = "https://api.umbrella.com"
access_token_endpoint = f"{base_url}/auth/v2/token"
all_activites_url = f"{base_url}/reports/v2/activity"


def generate_access_token():

    response = requests.post(url=access_token_endpoint,auth=(client_key,client_secret))
    access_token = response.json()['access_token']
    return access_token

# List all activity entries (dns/proxy/firewall/intrusion) from Umbrella for the past 7 days until now. 
def get_umbrella_activites(access_token, domain):  

    headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json",
    "Accept": "application/json"
    } 
    params = {
            "from": "-7days",
            "to": "now",
            "limit": 1000
        }
    url = all_activites_url

    get_activites = requests.get(url, headers=headers, params=params)
    all_activites = get_activites.text

    return all_activites


access = generate_access_token()
print(get_umbrella_activites(access))