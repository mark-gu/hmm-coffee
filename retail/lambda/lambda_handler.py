import os
import json
import boto3
import random
import requests
from requests_aws4auth import AWS4Auth
import coffeeTransaction

service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, 'ap-southeast-2', service, session_token=credentials.token)


headers = { "Content-Type": "application/json" }

# publish order information in bulk
def lambdaSnsPublisher(event, context):
  host = 'https://???.ap-southeast-2.es.amazonaws.com/'
  url = host + 'coffee-retail/_doc'
  print(url)

  minOrdersPerMin=int(os.environ['minOrdersPerMin'])
  maxOrdersPerMin=int(os.environ['maxOrdersPerMin'])
  numOfOrders=random.randint(minOrdersPerMin,maxOrdersPerMin)

  for x in range(numOfOrders):
    message = coffeeTransaction.getDummyCoffeeOrder()
    response = requests.post(url, auth=awsauth, json=message, headers=headers)

  print("Published: "+str(numOfOrders) + "  messages !!!")
