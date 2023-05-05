from django.contrib import admin
from crud.models import Users
from crud.models import Demande_Emprunt
from crud.models import PreuvRembEmpr
from crud.models import Preuv_Cotisation
from crud.models import Preuv_Cotis_Sinistre
from crud.models import Annonces
from crud.models import Cotisation_Sinistre
from crud.models import Autre_Cotisation
from crud.models import Infos_Emprunt
from crud.models import Infos_Sinistre
from crud.models import Infos_Cotisation
from crud.models import Mutuelle
from crud.models import Enregistrement_Emprunt

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id_users', 'photo', 'noms', 'prenoms', 'sexe', 'pays', 'ville', 'date_creation', 'statut', 'phone')

class Demande_EmpruntAdmin(admin.ModelAdmin):
    list_display = ('id_demande', 'beneficiaire', 'montant', 'interet', 'date_remboursement', 'motif')

class PreuvRembEmprAdmin(admin.ModelAdmin):
    list_display = ('id_preuve', 'noms_membre', 'montant_attendu', 'montant_verser', 'interet', 'reste', 'justificatifs')

class Preuv_CotisationAdmin(admin.ModelAdmin):
    list_display = ('id_preuve','nature_cotisation','noms_membre', 'montant_attendu', 'montant_verser', 'interet', 'reste', 'justificatifs')

class Preuv_Cotis_SinistreAdmin(admin.ModelAdmin):
    list_display = ('id_preuve','nature_sinistre','noms_membre', 'montant_attendu', 'montant_verser', 'interet', 'reste', 'justificatifs')

class AnnoncesAdmin(admin.ModelAdmin):
    list_display = ('id_annonce', 'objet', 'libelle', 'destinataire', 'date')

class Cotisation_SinistreAdmin(admin.ModelAdmin):
    list_display = ('id_cotisation', 'beneficiaire', 'nom_cotisant', 'montant_attendu', 'montant_verser', 'date', 'reste')

class Autre_CotisationAdmin(admin.ModelAdmin):
    list_display = ('id_cotisation','type_cotisation','autre_type', 'beneficiaire', 'nom_cotisant', 'montant_attendu', 'montant_verser','interet', 'date', 'reste')

class Infos_EmpruntAdmin(admin.ModelAdmin):
    list_display = ('id_infos', 'beneficiaire', 'description', 'montant', 'raison', 'date_remboursement', 'interet')

class Infos_SinistreAdmin(admin.ModelAdmin):
    list_display = ('id_infos','type_sinistre','autre_type','beneficiaire', 'description', 'montant', 'raison', 'date_remboursement', 'interet')

class Infos_CotisationAdmin(admin.ModelAdmin):
    list_display = ('id_infos','type_cotisation','autre_type','beneficiaire', 'description', 'montant', 'raison', 'date_remboursement', 'interet')

class MutuelleAdmin(admin.ModelAdmin):
    list_display = ('id_mutuelle', 'logo', 'abbreviation', 'nom_association', 'date_creation', 'statut_association', 'reglement_interieur')

class Enregistrement_EmpruntAdmin(admin.ModelAdmin):
    list_display = ('id_enregistrement', 'emprunteur', 'montant_attendu', 'montant_verser', 'reste', 'interet', 'date_remboursement', 'raison_emprunt')

admin.site.register(Users, UsersAdmin)
admin.site.register(Demande_Emprunt)
admin.site.register(PreuvRembEmpr)
admin.site.register(Preuv_Cotisation)
admin.site.register(Preuv_Cotis_Sinistre)
admin.site.register(Annonces)
admin.site.register(Cotisation_Sinistre)
admin.site.register(Autre_Cotisation)
admin.site.register(Infos_Emprunt)
admin.site.register(Infos_Sinistre)
admin.site.register(Infos_Cotisation)
admin.site.register(Mutuelle)
admin.site.register(Enregistrement_Emprunt)


# Register your models here.
