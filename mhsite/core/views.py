from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import LoginForm, SignUpForm
from .models import MessCut

def index(request):
    if request.user.is_authenticated():
        name = request.user.username
    else:
        name = "Home"
    return render(request, "core/index.html", {'name': name})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'core/login.html', {'form': form})
        else:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            user_login(request, user)
            return redirect('/')
        else:
            return redirect('/login')    
    else:
        form = LoginForm()
        return render(request, 'core/login.html', {'form': form})    


def logout(request):
    user_logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'core/signup.html',
                            {'form' : form})
        else:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            User.objects.create_user(username=username, email=email,
                                        password=password)
            user = authenticate(username=username, password=password)
            user_login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
        return render(request, 'core/signup.html',
                        {'form' : form})


def mess(request):
    if request.user.is_authenticated():
        status_cuts = []
        user_id = request.user.id
        mess_cuts = MessCut.objects.filter(user_id=user_id)
        for i, mess_cut in enumerate(mess_cuts):
            if mess_cut.status == False:
                status_cuts.append((mess_cut, "Pending"))
        status = True
    else:
        mess_cuts = []
        status = False
    name = "Home"

    if request.method == "POST":
        mess = MessCut()
        mess.user_id = request.user.id
        mess.start_date = request.POST["startdate"]
        mess.end_date = request.POST["enddate"]
        mess.days = int(request.POST["noofdays"])
        result = mess.save()
        print(result)
        return redirect('/mess')
    else:
        return render(request, "core/mess.html", {'name': name, 
                                                    'mess_cuts': status_cuts, 'status': status})



def contact(request):
    if request.user.is_authenticated():
        name = request.user.username
    else:
        name = "Home"
    return render(request, "core/contact.html", {'name': name})

def gallery(request):
    if request.user.is_authenticated():
        name = request.user.username
    else:
        name = "Home"
    return render(request, "core/gallery.html", {'name': name})

def studentscorner(request):
    if request.user.is_authenticated():
        name = request.user.username
    else:
        name = "Home"
    return render(request, "core/studentscorner.html", {'name': name})