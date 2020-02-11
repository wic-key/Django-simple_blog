from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegistrationSerializer


# Create your views here.


@api_view(['POST'])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







def home(request):
    template = 'demosite/home.html'
    return render(request,template)



@api_view(['GET','POST'])   
def index(request):
    print(request.user)
    print(request.auth)
    if request.method=='GET':
        return Response(data={'message':'this is django apis'})
    elif request.method=='POST':
        print(request.data)
        return Response(data=request.data,status=status.HTTP_200_OK)
    else:
        return Response('this is not a valid request method')


class Message(APIView):
    def get(self,request):
        return Response(data={'message':'this is class base api'},status=status.HTTP_200_OK)



def login(request):
    template = 'demosite/login.html'
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.info(request,'Login successfully')
            return redirect('home')
        else:
            messages.info(request,'invalid cridential')
            return redirect('login')
    else:
        return render(request,template)

def logout(request):
    auth.logout(request)
    return redirect('home')



def register(request):
    template = 'demosite/register.html'
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username  already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already Taken')
                return redirect('register') 
            else:                    
                user = User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info('password not matching')
            return redirect('register')
            
    else:
        return render(request,template)

def getstart(request):
    if request.user.is_authenticated:
        return render(request,'demosite/getstart.html')
    else:
        return redirect(login)