from django.shortcuts import render, redirect
from crud.models import Users
from crud.models import Mutuelle
from .forms import PreuvRembEmprForm, DemandeEmpruntForm
from django.urls import reverse

def connexion(request):
    return render(request, 'crud/connexion.html')

def index(request):
    return render(request, 'crud/index.html')

def support(request):
    return render(request, 'crud/support.html')

def annonce(request):
    association = Mutuelle.objects.all()
    return render(request, 'crud/annonces.html', context={"assoc":association})

def association(request):
    association = Mutuelle.objects.all()
    return render(request, 'crud/association.html', context={"assoc":association})

def cotisation(request):
    return render(request, 'crud/cotisation.html')

def cslter_empr(request):
    return render(request, 'crud/cslter_empr.html')

def dmd_emprunt(request):
    form=DemandeEmpruntForm()
    if request.method=="POST":
        form=DemandeEmpruntForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("demander_emp"))
        
    return render(request, 'crud/dmd_emprunt.html', {"form":form})

def enrg_remb(request):
    form=PreuvRembEmprForm()
    if request.method=="POST":
        form=PreuvRembEmprForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("enregistrement_remb"))
    return render(request, 'crud/enrg_remb.html', {"form":form})

def home(request):
    association = Mutuelle.objects.all()
    return render(request, 'crud/home.html',context={"assoc":association})

def prestation(request):
    return render(request, 'crud/prestation.html')

def reporting(request):
    return render(request, 'crud/reporting.html')

def utilisateur(request):    
    association = Mutuelle.objects.all()
    users = Users.objects.all()
    return render(request, 'crud/utilisateur.html',context={"users": users, "assoc":association})  