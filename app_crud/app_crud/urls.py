from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('connexion/', views.connexion,name="connexion"),
    path('index/', views.index,name="index"),
    path('support/', views.support,name="support"),
    path('annonce/', views.annonce,name="annonce"),
    path('association/',views.association,name="association"),
    path('cotisation/', views.cotisation,name="cotisation"),
    path('consulter_empr/', views.cslter_empr,name="consulter_emp"),
    path('demander_empr/', views.dmd_emprunt,name="demander_emp"),
    path('enregistrer_remb/', views.enrg_remb,name="enregistrement_remb"),
    path('home/', views.home,name="home"),
    path('prestation/', views.prestation,name="prestation"),
    path('reporting/', views.reporting,name="reporting"),
    path('utilisateur/', views.utilisateur,name="utilisateur")
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
