# Trustpilot-Salesforce-API-Integration
Trustpilot Integration with Salesforce using simple-salesforce and Trustpilot API (generate service review invitation link)

This integation uses [Python Simple-Salesforce package](https://pypi.org/project/simple-salesforce/). This integration does **NOT** use Scratch Orgs or Salesforce DX Environment. Rather, this can be run completely from your own CLI completely outside of Salesforce Developer Experience.

# Summary
This integration gathers all contacts within your Salesforce account, creates a verified invitation link using Trustpilot's API, then adds that verified link into a contact field in Salesforce.

## Installation 
pip install simple-salesforce (https://pypi.org/project/simple-salesforce/)

## Authentication and Customization
**Salesforce Authentication**
- username = your Salesforce username used to login 
- password = your Salesforce password used to login
- security_token = your Salesforce account security token - can be reset following [these instructions](https://onlinehelp.coveo.com/en/ces/7.0/administrator/getting_the_security_token_for_your_salesforce_account.htm)



**Trustpilot Authentication**
Trustpilot Customer APIs contain private resources and use OAuth 2.0 authentication. In order to access private resources, you need an access token. In this program we use [Grant Type: Password](https://developers.trustpilot.com/authentication#password).

- username = your Trustpilot username used to login to [Trustpilot](https://business.trustpilot.com/)
- password = your Trustpilot password used to login
- apiKey & secret = your Trustpilot API key. This can be found in the Integrations tab, in the API section of your account. Follow [these instructions to generate or find your keys](https://support.trustpilot.com/hc/en-us/articles/207309867-Getting-started-with-Trustpilot-s-APIs).
- businessUnitId = The business unit ID is a unique identifier for that business unit and is the primary key in many of your API calls. You can find this by calling the API endpoint ["find a business unit"](https://developers.trustpilot.com/business-units-api#find-a-business-unit). More instructions can be found [here](https://developers.trustpilot.com/tutorials/how-to-find-your-business-unit-id). 

Your returned access token should be appended to the url of any private Trustpilot API calls. You'll see this as the auth_token value in the script. 

## Salesforce Information
Use the query call to query your Salesforce contacts. We will need name, email address and a unique identifying number as a minimum of fields that will be passed to Trustpilot. The identifying number can be anything, such as a custom contact field for account number or order number. In this script we're using Salesforce's generated unique ID, but it should be a number you can easily associate with this customer's experience with you so that you can easily look them up by their unqiue reference ID if necessary. 

## Use Customer Data to Generate A Unique Trustpilot Review Link 
Perform a POST call to Trustpilot's API with your Business Unit Id, OAuth Token, and Customer Data. If the call was successful, a unique link will be returned per Salesforce contact. More information on this API call can be found [here](https://developers.trustpilot.com/invitation-api#generate-service-review-invitation-link). See [frequently asked questions](https://developers.trustpilot.com/faq) for common error messages. 

## Update Salesforce with the Trustpilot Unique Link
Use the update call to update any field with the unique link returned from Trustpilot. In this script we're using the Salesforce "Description" field to host the Trustpilot Invitation link but this can be any field. I would recommend a custom contact field called "Trustpilot invitation link". Use this field in any communications sent from Salesforce as data tag to dynamically populate this link for each customer. 
