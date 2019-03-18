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
- username = your Trustpilot username used to login to [Trustpilot](https://business.trustpilot.com/)
- password = your Trustpilot password used to login
- apiKey & secret = your Trustpilot API key. This can be found in the Integrations tab, in the API section of your account. Follow [these instructions to generate or find your keys](https://support.trustpilot.com/hc/en-us/articles/207309867-Getting-started-with-Trustpilot-s-APIs).
- businessUnitId = The business unit ID is a unique identifier for that business unit and is the primary key in many of your API calls. You can find this by calling the API endpoint ["find a business unit"](https://developers.trustpilot.com/business-units-api#find-a-business-unit). More instructions can be found [here](https://developers.trustpilot.com/tutorials/how-to-find-your-business-unit-id). 
