import ssl
from django.shortcuts import render
from django.http import HttpResponse

import pymongo
import certifi
ca = certifi.where()

# client = pymongo.MongoClient("mongodb+srv://razak:mohamed@cluster0.ptmlylq.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)
# db = client['forenoon']

from mongoengine import connect

from . import documents

#client=connect(host="mongodb+srv://razak:mohamed@cluster0.ptmlylq.mongodb.net/forenoon?retryWrites=true&w=majority")
client=connect(db="forenoon", host="mongodb+srv://razak:mohamed@cluster0.ptmlylq.mongodb.net/forenoon?retryWrites=true&w=majority", username="razak", password="mohamed",tlsCAFile=ca)



# Create your views here.

def fetch(req):
    print(client)
    # s1=documents.Candidate()
    # s1.age=26
    # s1.name="Annamalai S"
    # s1.studentid=87654567
    # s1.save()
    hey=documents.Candidate.objects
    for x in hey:
        print(str(x))
    return HttpResponse("<h1>HAI</h1>")