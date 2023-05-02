from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Users(models.Model):
    SEXE = [       
        ("M","Masculin"),
        ("F","Feminin"),
    ]
    PAYS = [
        ("CMR","Cameroun"),
    ]
    VILLE = [
        ("YDE","Yaounde"),("DLA","Douala"),("GAR","Garoua"),("MAR","Maroua"),("BER","Bertoua"),("EBOL","Ebolowa"),("BUEA","Buea"),("NGA","Ngaoundere"),("BAM","Bamenda"),("BAF","Bafoussam"),
    ]
    STATUT = [
        ("TRES","TRESORIER"),("SECR","SECRETAIRE"),("ASSIS TRES","ASSISTANT TRESORIER"),("REPORT","REPORTEUR"),
    ]    
    id_users = models.AutoField(primary_key=True,blank=False)
    photo = models.ImageField(blank=True)
    noms = models.fields.CharField(max_length=20, blank=False)
    prenoms = models.fields.CharField(max_length=20, blank=False)
    sexe = models.CharField(max_length=1, choices=SEXE ,blank=False)
    pays = models.fields.CharField(max_length=20, blank=False, choices=PAYS)
    ville = models.fields.CharField(max_length=20, blank=False, choices=VILLE)
    date_creation = models.DateField( blank=False)
    statut = models.fields.CharField(max_length=30, blank=False, choices=STATUT)
    e_mail = models.fields.CharField(max_length=20, blank=False)
    phone = models.IntegerField( blank=False)
    username = models.fields.CharField(max_length=20, blank=False)
    password = models.fields.CharField(max_length=20, blank=False)
    pass
  
    
class Demande_Emprunt(models.Model):
    users = models.ForeignKey(Users,on_delete=models.CASCADE)
    id_demande = models.AutoField(primary_key=True,blank=False)
    beneficiaire = models.fields.CharField(max_length=30,blank=False)
    montant = models.FloatField(blank=False)
    interet = models.FloatField(blank=False)
    date_remboursement = models.DateField(blank=False)
    motif = models.fields.CharField(max_length=80,blank=False)
    
   
class Preuve(models.Model):
    users = models.ForeignKey(Users,on_delete=models.CASCADE)
    id_preuve = models.AutoField(primary_key=True,blank=False)
    noms_membre = models.fields.CharField(max_length=50,blank=False)
    montant_attendu = models.FloatField(blank=False)
    montant_verser = models.FloatField(blank=False)
    date = models.DateField(blank=False)
    justificatifs = models.FileField(blank=False)    
    class Meta:
        abstract = True
 
        
class Preuv_Remb_Empr(Preuve):
    reste = models.FloatField(blank=False)
    interet = models.FloatField(blank = False)
  
    
class Preuv_Cotisation(Preuve):
    nature_cotisation = models.fields.CharField(max_length=20,blank=False)
    

class Preuv_Cotis_Sinistre(Preuve):
    nature_sinistre = models.fields.CharField(max_length=20,blank=False)
    
    
class Annonces(models.Model):
    users = models.ForeignKey(Users,on_delete=models.CASCADE)
    id_annonce = models.AutoField(primary_key=True,blank=False)
    objet = models.fields.CharField(max_length=50,blank=False)
    libelle = models.fields.CharField(max_length=300,blank=False)
    destinataire = models.fields.CharField(max_length=30,blank=False)
    date = models.DateField(blank=False)
    
    
class Cotisation_Effective(models.Model):
    id_cotisation = models.AutoField(primary_key=True,blank=False)
    beneficiaire = models.fields.CharField(max_length=30,blank=False)
    nom_cotisant = models.fields.CharField(max_length=30,blank=False)
    montant_attendu = models.FloatField(blank=False)
    montant_verser = models.FloatField(blank=False)
    reste = models.FloatField(blank=False)
    date = models.DateField(blank=False) 
    class Meta:
        abstract=True
        
        
class Cotisation_Sinistre(Cotisation_Effective):
    AUTRE = [
        ("Maladie","Maladie"),
        ("Accident","Accident"),
        ("Deuil","Deuil"),
        ("Accouchement","Accouchement"),
    ]
    type_sinistre = models.fields.CharField(max_length=60,blank=True,choices=AUTRE)
    autre_type = models.fields.CharField(max_length=60,blank=True)
    
class Autre_Cotisation(Cotisation_Effective):
    AUTRE = [
        ("Epargne","Epargne"),
    ]
    type_cotisation = models.fields.CharField(max_length=60,blank=True,choices=AUTRE)
    autre_type = models.fields.CharField(max_length=60,blank=True)
    interet = models.FloatField(blank=False)
    
    
class Infos(models.Model):
    id_infos = models.AutoField(primary_key=True,blank=False)
    beneficiaire = models.fields.CharField(max_length=30 ,blank=False)
    description = models.fields.CharField(max_length=300,blank=False)
   
class Infos_Emprunt(Infos):
    montant = models.FloatField(blank=False)
    raison = models.fields.CharField(max_length=50,blank=False)
    date_remboursement = models.DateField(blank=False)
    interet  = models.FloatField(blank=False)
    
class Infos_Sinistre(Infos):
    AUTRE = [
        ("Maladie","Maladie"),
        ("Accident","Accident"),
        ("Deuil","Deuil"),
        ("Accouchement","Accouchement"),
    ]
    type_sinistre = models.fields.CharField(max_length=30,blank=False,choices=AUTRE)
    autre_type = models.fields.CharField(max_length=60,blank=True)
    
class Infos_Cotisation(Infos):
    AUTRE = [
        ("Maladie","Maladie"),
        ("Accident","Accident"),
        ("Deuil","Deuil"),
        ("Accouchement","Accouchement"),
    ]
    type_cotisation = models.fields.CharField(max_length=30,blank=True,choices=AUTRE)
    autre_type = models.fields.CharField(max_length=60,blank=True)


class Mutuelle(models.Model):
    id_mutuelle = models.AutoField(primary_key=True,blank=False)
    logo = models.ImageField(blank=True)
    abbreviation = models.fields.CharField(max_length=30,blank=False)
    nom_association = models.fields.CharField(max_length=50,blank=False)
    date_creation = models.DateField(blank=False)
    statut_association = models.fields.CharField(max_length=100,blank=False)
    reglement_interieur = models.fields.CharField(max_length=20,blank=False)
    
    
class Enregistrement_Emprunt(models.Model):
    id_enregistrement = models.AutoField(primary_key=True,blank=False)
    emprunteur = models.fields.CharField(max_length=50,blank=False)
    montant_attendu = models.FloatField(blank=False)
    montant_verser = models.FloatField(blank=False)
    reste = models.FloatField(blank=False)
    interet = models.FloatField(blank=False)
    date_remboursement = models.DateField(blank=False)
    raison_emprunt = models.fields.CharField(max_length=300,blank=False)