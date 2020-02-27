from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('portfolio/', views.PortfolioListView.as_view(), name='portfolio'),
    path('species/', views.SpeciesListView.as_view(), name='species'),
    path('species/<int:pk>', views.SpeciesDetailView.as_view(), name='species-detail'),
    path('family/', views.FamilyListView.as_view(), name='family'),
    # path('family/<slug:str>', views.FamilyDetailView.as_view(), name='family-detail'),
    path('familyspecification/<slug:str>', views.FamilySpecificationDetailView.as_view(), name='familyspecification-detail'),
    # path('variety/<slug:str>', views.VarietyDetailView.as_view(), name='variety-detail'),
    path('variety/<int:pk>', views.VarietyDetailView.as_view(), name='variety-detail'),
]