import requests
from dotenv import load_dotenv 
import os

# Access token generation requires that the user has a valid Umbrella API Key and Secret: https://developer.cisco.com/docs/cloud-security/#!authentication/manage-api-keys

load_dotenv()

# Environmental variables should contain your org's values in .env file.
client_key = os.environ['API_KEY']
client_secret = os.environ['KEY_SECRET']

# Relevant v2 Umbrella API endpoints
base_url = "https://api.umbrella.com"
access_token_endpoint = f"{base_url}/auth/v2/token"

# Generate new access token as these expire after 1 hour. Requires a valid and unexpired Umbrella API Key and Key Secret.
def generate_access_token():

    response = requests.post(url=access_token_endpoint,auth=(client_key,client_secret))
    access_token = response.json()['access_token']

    return access_token