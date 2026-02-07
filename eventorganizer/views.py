from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Oraganizerdata
from .models import Registeredto
#from django.contrib.auth.models import User
# Create your views here.

def organizerhome(request):
    return render(request,"organizerhome.html")
def datadb(request):
    if request.method=='POST':
        eid=request.POST.get('eventId')
        ename=request.POST.get('eventName')
        eloc=request.POST.get('eventLocation')
        eimg=request.POST.get('eventImage')
        etim=request.POST.get('eventTime')
        edate=request.POST.get('eventDate')
        ecost=request.POST.get('eventCost')
        orginfo=request.POST.get('organizerInfo')

        if eid and ename and eloc and eimg and etim and edate and ecost and orginfo:
            Oraganizerdata.objects.create(event_Id=eid,event_Name=ename,event_Location=eloc,event_Image=eimg
                                          ,event_Time=etim,event_Date=edate,event_Price=ecost,event_orginfo=orginfo)
            return render(request,'success.html')
        else:
            return HttpResponse("<h1>FAILED</h2>")
    return render(request,"organizerhome.html")
def showevents(request):
    eventdata=Oraganizerdata.objects.all()
    return render(request,"Showevents.html",{'events':eventdata})

def proceedtopay(request):
    if request.method=="POST":
        event=request.POST['eventname']
        eventid=request.POST['eventid']
        user=request.POST['username']
        userid=request.POST['userid']
        #organizerid=""+request.POST['organizerid']
        if event and eventid and user and userid:
            Registeredto.objects.create(userid=userid,username=user,eventid=eventid,eventname=event,organizerid=32)
            return render(request,"success.html")
        else:
            return HttpResponse(request,"<h1>FAILED TO RECORD YOUR REGISTRATION</h1>")

        print("event=",event)
        return render(request,"payment.html")
    else:
        return HttpResponse(request,"<h1>Data not came through post</h1>")
    #return redirect("payment.html")
    return render(request,"payment.html")
#If payment success then will be registered
def register(request):
    return HttpResponse(request,"<h1>Registered</h1>")
def home(request):
    eventdata=Oraganizerdata.objects.all()
    return render(request,"home.html",{'events':eventdata})
    #return render(request,"home.html",{''})