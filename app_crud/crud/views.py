from django.shortcuts import render
from crud.models import Users
from crud.models import Mutuelle

def connexion(request):
    return render(request, 'crud/connexion.html')

def index(request):
    return render(request, 'crud/index.html')

def support(request):
    return render(request, 'crud/support.html')

def annonce(request):
    return render(request, 'crud/annonces.html')

def association(request):
    association = Mutuelle.objects.all()
    return render(request, 'crud/association.html', context={"assoc":association})

def cotisation(request):
    return render(request, 'crud/cotisation.html')

def cslter_empr(request):
    return render(request, 'crud/cslter_empr.html')

def dmd_emprunt(request):
    return render(request, 'crud/dmd_emprunt.html')

def enrg_remb(request):
    return render(request, 'crud/enrg_remb.html')

def home(request):
    return render(request, 'crud/home.html')

def prestation(request):
    return render(request, 'crud/prestation.html')

def reporting(request):
    return render(request, 'crud/reporting.html')

def utilisateur(request):
    users = Users.objects.all()
    return render(request, 'crud/utilisateur.html',context={"users": users})  