from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.ContactList.as_view(), name='contacts'),
    path('contact/<int:pk>', views.ContactDetail.as_view(), name='contact-detail'),
    path('contact/create', views.contact_create, name='contact_create'),
    path('contact/types/', views.ContactTypeList.as_view(), name='contact-types'),
    path('contact/type/<int:pk>', views.ContactTypeDetail.as_view(), name='contact-type-detail'),
    path('contact/type/create', views.contact_type_create, name='contact_type_create'),
    path('contact/entities/', views.EntityList.as_view(), name='entities'),
    path('contact/entity/<int:pk>', views.EntityDetail.as_view(), name='entity-detail'),
    path('contact/entity/create', views.entity_create, name='entity_create'),
    path('contact/persons/', views.PersonList.as_view(), name='persons'),
    path('contact/person/<int:pk>', views.PersonDetail.as_view(), name='person-detail'),
    path('contact/person/create', views.person_create, name='person_create'),
]
