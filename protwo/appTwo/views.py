from django.shortcuts import render
from appTwo.models import User
from appTwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request, 'appTwo/index.html')

def users_info(request):
    users_list = User.objects.all()
    return render(request, 'appTwo/users_info.html', {'users': users_list})

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error') 

    return render(request, 'appTwo/users.html', {'form': form})


    