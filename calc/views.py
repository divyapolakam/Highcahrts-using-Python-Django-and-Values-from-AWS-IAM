import boto3
from boto3.dynamodb.conditions import Key, Attr
from django.shortcuts import render
# Create your views here.

db=boto3.resource("dynamodb")
table=db.Table("Internship")

def home(request):
    response=table.scan()
    items = response['Items']
    while 5 in response:
        print(response['5'])
        response = table.scan(ExclusiveStartKey=response[5])
        items.extend(response['Items'])
    return render(request, "home.html", {'dataset': items})

