from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views import generic
# Create your views here.

from todo.models import TodoList




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


def register_view(request):
    if request.method == "GET":
        return render(request, 
                  'registration/register.html', 
                  )

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username, password=password)
        user.save()
        return HttpResponse("done")


class TodoListView(generic.ListView):
    template_name   = 'todo/index.html'
    context_object_name = 'all_todo_lists'

    def get_queryset(self):
        return TodoList.objects.filter(author=self.request.user)
