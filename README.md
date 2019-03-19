# Trustpilot-Salesforce-Integration
Trustpilot Integration with Salesforce using simple-salesforce and Trustpilot API (generate service review invitation link)

This integation uses [Python Simple-Salesforce package](https://pypi.org/project/simple-salesforce/). 

# Installation 
pip install simple-salesforce (https://pypi.org/project/simple-salesforce/)

## Authentication and Customization
**SalesForce Authentication**
- username = your SalesForce username used to login 
- password = your SalesForce password used to login
- security_token = your SalesForce account security token - can be reset following [these instructions](https://onlinehelp.coveo.com/en/ces/7.0/administrator/getting_the_security_token_for_your_salesforce_account.htm)



**Trustpilot Authentication**
Trustpilot Customer APIs contain private resources and use OAuth 2.0 authentication. In order to access private resources, you need an access token. In this program we use [Grant Type: Password](https://developers.trustpilot.com/authentication#password).

- username = your Trustpilot username used to login to [Trustpilot](https://business.trustpilot.com/)
- password = your Trustpilot password used to login
- apiKey & secret = your Trustpilot API key. This can be found in the Integrations tab, in the API section of your account. Follow [these instructions to generate or find your keys](https://support.trustpilot.com/hc/en-us/articles/207309867-Getting-started-with-Trustpilot-s-APIs).
- businessUnitId = The business unit ID is a unique identifier for that business unit and is the primary key in many of your API calls. You can find this by calling the API endpoint ["find a business unit"](https://developers.trustpilot.com/business-units-api#find-a-business-unit). More instructions can be found [here](https://developers.trustpilot.com/tutorials/how-to-find-your-business-unit-id). 

Your returned access token should be appended to the url of any private Trustpilot API calls. You'll see this as the auth_token value in the script. 

