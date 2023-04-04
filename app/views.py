from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def inserttopic(request):
    tn=input('enter the topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('data inserted successfully')
def insertwebpage(request):
    tn=input('enter the topic name')
    n=input('enter the name')
    url=input('enter the url')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    return HttpResponse('data inserted successfully')
def insertrecord(request):
    tn=input('enter the topic name')
    n=input('enter the name') 
    url=input('enter the url')
    no=input('enter sl no')
    aut=input('enter the author')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    RO=Records.objects.get_or_create(slno=no,name=WO,author=aut)[0]
    RO.save()
    return HttpResponse('data inserted successfully')


def displaytopic(request):
    LOT=Webpage.objects.all()
    LOR=Records.objects.all()
    d={'topics':LOT,'records':LOR}
    return render(request,'displaytopic.html',d)

