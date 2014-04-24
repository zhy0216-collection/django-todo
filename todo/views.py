from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.






'''
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:

        login(request, user)
        # redirect to index

    else:
        # flash invalid login
        pass
'''

def logout_view(request):
    logout(request)
    # redirect to index



