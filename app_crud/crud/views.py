from django.shortcuts import render

def connexion(request):
    return render(request, 'crud/connexion.html')

def index(request):
    return render(request, 'crud/index.html')

def support(request):
    return render(request, 'crud/support.html')

def annonce(request):
    return render(request, 'crud/annonces.html')

def association(request):
    return render(request, 'crud/association.html')

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
    return render(request, 'crud/utilisateur.html')