
from django import forms
import django
from .models import PreuvRembEmpr, Demande_Emprunt

class PreuvRembEmprForm(forms.ModelForm):

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        for _ in self.fields.values():
            _.widget.attrs.update({"class":"cont"})
        
    class Meta:
        model=PreuvRembEmpr
        fields=["noms_membre",
         "montant_attendu",
         "montant_verser",
         "date",
         "justificatifs",
         "reste",
         "interet"]

class DemandeEmpruntForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        for _ in self.fields.values():
            _.widget.attrs.update({"class":"cont"})
        
    class Meta:
        model=Demande_Emprunt
        fields=[
        "beneficiaire",
         "montant",
         "interet",
         "date_remboursement",
         "motif",]

    