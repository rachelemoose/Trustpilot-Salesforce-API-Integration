import requests
import json
from simple_salesforce import Salesforce
from requests.auth import HTTPBasicAuth

# Salesforce Authentication - login using the security token method, simply include the Salesforce method and pass in your Salesforce username, password and token (this is usually provided when you change your password):
sf = Salesforce(username='your_sf_username', password='your_sf_password', security_token='sf_security_token')
