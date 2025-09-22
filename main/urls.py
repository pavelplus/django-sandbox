from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', views.person_list, name='persons'),
    path('persons/create/', views.person_create, name='create_person'),
    path('persons/edit/<int:id>/', views.person_edit, name='edit_person'),
    path('persons/delete/', views.person_delete, name='delete_person'),
]