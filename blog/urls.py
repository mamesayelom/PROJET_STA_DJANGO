from django.urls import path,include
from .views import ActiviteListview,DashboardListview,AjouterActiviteView,ActiviteUpdateView,ActiviteDeleteView,DetailActiviteView,InscriptionView

urlpatterns = [
    path('', DashboardListview.as_view(),name='dasboard'),
    path('activites/', ActiviteListview.as_view(),name='liste_activite'),
    path('ajouter/activite/',AjouterActiviteView.as_view(),name='ajouter_activite'),
    path('activite/<int:pk>/edit/', ActiviteUpdateView.as_view(), name='activite_edit'),
    path('activite/<int:pk>/delete/', ActiviteDeleteView.as_view(), name='activite_delete'),
    path('detail/<int:pk>/activite/', DetailActiviteView.as_view(),name='detail_activite'),
    path('inscription/',InscriptionView.as_view(),name='inscription'),
]