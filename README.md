# Cisco-Umbrella-Automation
A repository of sample Umbrella scripts for network automation professionals to choose from when creating automated workflows

## Sample Python Scripts & API Calls Included
* **Authenticate with Umbrella** - generate_umbrella_access_token.py calls the API key and key secret you created from a .env file and uses them to generate an access token (expires in 1 hour)
* **Find uncommon domains accessed in your network(s)** - find_uncommon_domains_with_umbrella.py automatically finds domains outside of Umbrella's top 1 million (posted daily) for potential investigation and/or action
* **Get a domain's security score** - get_domain_security_score.py retrieves the Umbrella risk score for a single domain, with 0 being no risk at all and 100 being the highest. More info: https://developer.cisco.com/docs/cloud-security/legacy-umbrella-apis-investigate-api-reference-api-security-information-for-a-domain-get-risk-score-for-domain/
* **Reporting the past week's DNS requests** - 
* **Create a ticket in Jira for investigation and incident response** - create_jira_ticket.py


## Requirements
* Access to active Cisco Umbrella account OR Cisco DevNet Umbrella sandbox:
* Umbrella Admin API key. (Please see documentation to apply a reasonable scope relevant to the scripts you are interested in using: https://developer.cisco.com/docs/cloud-security/oauth-2-0-scopes/)
* VS Code 1.87.0 (or IDE of your choice)
* Python 3.12.1
* Python libraries listed in '''requirements.txt''' (see below, Run Project, to install)

## Installation & Usage
### Install VS Code & Python

* If you do not have VS Code or another IDE, you may download and install VS Code for your OS here: https://code.visualstudio.com/download.
* If you do not have Python3, choose your OS and download python here: https://www.python.org/downloads/. Then, follow the installation instructions here based on your OS: https://kinsta.com/knowledgebase/install-python/#how-to-install-python.
* If you will be cloning this repository as indicated in the instructions of the next section, you will need to install git. (If you are not comfortable with this, in the GitHub repository, simply choose 'Download Zip'): https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

### Create Umbrella Admin API Key
1. Login to the Umbrella dashboard:
 * Umbrella customers: ```https://login.umbrella.com/```
 * Umbrella sandbox users: ```https://devnetsandbox.cisco.com/DevNet/catalog/umbrella-secure-internet-gateway```
2. In the leftside menu, navigate to Admin > API Keys
3. Click the plus symbol in the top right of the screen that says “Add.”
4. For the Key Scope, choose the appropriate level of scope for the script being run: https://developer.cisco.com/docs/cloud-security/oauth-2-0-scopes/
5. Choose a date that isn't today for the API expiration date (or click “Never expires”).
6. Save the generated API Key and Key Secret, as we will be using this in the project.
    
### Run Project
* Clone this repository:
```git clone https://github.com/erdietri/Cisco-Umbrella-Automation.git```
* Navigate to the project directory:
```cd umbrellauncommondomains```
* Install the dependencies:
```pip install -r requirements.txt```
* Add your API Key and Key Secret values to the .env file. (Simply copy/paste. They do not need to be formatted as strings.)
* Run the Python script:
```python3 <insert-file-name>.py```

## Contributors
Erika Dietrick

## License
Copyright 2024 Erika Dietrick

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.