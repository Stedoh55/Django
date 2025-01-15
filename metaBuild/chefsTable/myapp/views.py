from django.shortcuts import render
from .models import Menu
from .forms import InputForm

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "index.html")

def about(request):
    heroes = {'hero':[
        {'name':'Holo Bundala','class':'BSN 4'},
        {'name':'Lucy Richard','class':'BSN 3'},
        {'name':'James Benjamin','class':'BSN 2'},
        {'name':'Andrew Johnson','class':'DNS 2'},
        {'name':'Aggrey Mrassu','class':'DNS 3'}
    ]}
    return render(request, 'about.html', heroes)

def usambara_menu(request):
    menu_list = Menu.objects.all()
    our_foods = {'menu': menu_list}
    return render(request, 'menu.html',our_foods)


def our_form(request):
    form = InputForm()
    context = {'form': form}
    return render(request, 'form.html', context)
