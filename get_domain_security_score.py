# This script is used to get the security score of a domain using the Umbrella Investigate API.
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
domain_security_score_endpoint = f"{base_url}/investigate/v2/security/name/"

# Generate new access token as these expire after 1 hour. Requires a valid and unexpired Umbrella API Key and Key Secret.
def generate_access_token():

    response = requests.post(url=access_token_endpoint,auth=(client_key,client_secret))
    access_token = response.json()['access_token']
    return access_token

# Get domain security score of 1 domain
def get_domain_security_score(access_token, domain):  

    headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json",
    "Accept": "application/json"
    } 

    url = domain_security_score_endpoint + domain

    domain_score_request = requests.get(url, headers=headers)
    domain_score = domain_score_request.text

    return domain_score

access = generate_access_token()
print(get_domain_security_score(access, 'google.com')) 