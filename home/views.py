from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

#password - satish@22
#password - sika@1999
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        #check if the user has entered correct credentials
        user = authenticate(request,username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")  

#def index(request):
    #return render(request,'index.html')
    #return HttpResponse("This is Homepage ")

def about(request):
    return render(request,'about.html')


def products(request):
    return render(request,'products.html')  

def Potatochips(request):
    return render(request,'Potatochips.html')

def TomatoKetchup(request):
    return render(request,'TomatoKetchup.html')  