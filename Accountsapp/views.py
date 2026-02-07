from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth,Group
# Create your views here.

#events_group=Group.objects.create(name="events_grp")

def signup(request):
    return render(request,"signup.html")
def signupinfo(request):
    if request.method=="POST":
        fname=request.POST['firstName']
        lname=request.POST['lastName']
        uname=request.POST['username']
        email=request.POST['email']
        pswd1=request.POST['password']
        pswd2=request.POST['confirmPassword']
        role=request.POST['role']
        '''if role=="organizer":
            group_name="organizers"
        elif role=="participant":
            group_name="participants"
        else:
            return HttpResponse(request,"<h1>Invalid Role</h1>")
        
        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            return HttpResponse("Group does not exist.")
        
        user.groups.add(group)'''

        user=User.objects.create_user(username=uname,password=pswd1,email=email,first_name=fname,last_name=lname)
        user.save()
        print("user created!")
        return redirect("login")
        #return HttpResponse("<h1>Sign in successful!</h><br><h3>user Inserted</h3>")
    return redirect('signuppage')
def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        pswd=request.POST['password']
        user=auth.authenticate(username=uname,password=pswd)
        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:
            return HttpResponse("<h1>wrong user cred!!</h1>")
        #return render(request,"userhome1.html",{'uname':uname})
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect("home")
