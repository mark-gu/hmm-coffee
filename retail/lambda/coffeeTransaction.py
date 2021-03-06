import uuid
import random
import json
from datetime import datetime, timedelta

##Global Config
coffeeNameList=["SageBrew","ElasticBean","CoffeeFormation"]
sizeList=["S","M","L"]
channels =["alexa","web","connect","button"]

def getProductFullList():

    productList=[]
    for coffeeName in coffeeNameList:
        for size in sizeList:
            product={
                "coffeeName":coffeeName,
                "size":size
            }
            productList.append(product)
    return productList

productFullList=getProductFullList()

def getDummyCoffeeOrder():
    orderId=str(uuid.uuid4())
    message={
     "orderId": orderId,
     "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
     "orderItems": getDummyItems(),
     "channel" : random.choice(channels),
     "orderPayable": 10.4
    }
    return message

def getDummyItems():
    orderItemList=random.sample(productFullList, random.randint(1,5))
    dummyItems=[]
    for orderItem in orderItemList:
        dummyItem=getDummyItem(orderItem["coffeeName"],orderItem["size"])
        dummyItems.append(dummyItem)
    return dummyItems

def getDummyItem(coffeeName,size):
    numberOfCups=[1,2,3,4]
    orderItem={
    "coffeeName": coffeeName,
    "number": random.choice(numberOfCups),
    "size": size
    }
    return orderItem
