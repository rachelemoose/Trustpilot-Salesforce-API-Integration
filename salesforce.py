import requests
import json
from simple_salesforce import Salesforce
from requests.auth import HTTPBasicAuth

# Salesforce Authentication - login using the security token method, simply include the Salesforce method and pass in your Salesforce username, password and token (this is usually provided when you change your password):
sf = Salesforce(username='your_sf_username', password='your_sf_password', security_token='sf_security_token')

# Trustpilot Authentication - Get Access Token and save as variable
header = {'grant_type':'password' , 'username':'yourtrustpilotlogin@email.com', 'password':'youTrustpilotPassword'}
apiKey = "YourTrustpilotApiKey" #APIKey
secret = "YourTrustpilotApiSecretKey" #Secret
businessUnitId = 'YourTPBUID' #Business Unit ID
response = requests.post(
    'https://api.trustpilot.com/v1/oauth/oauth-business-users-for-applications/accesstoken',
    auth=HTTPBasicAuth(apiKey, secret),  # basic authentication
    data=header)
# Making the content of the response it's own variable for auditing 
content = response.content
# Get response as parsed json
data = response.json()  
# See content in JSON format
print(data) 
# Get access token from JSON response
auth_token = data.get('access_token')
if auth_token == None:
	print('No Access Token Received')
else:
	print("Trustpilot Access Token: " + auth_token)
