from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('library/', views.library_page, name='library'),
    path('', views.welcome_page, name='welcome'),
    path('logout_user/', views.logout_user, name='logout'),
    path('signin/', views.signin_page, name='signin'),
    path('cautare/', views.cautare_carte, name='cautare'),
    path('adaugare/', views.add_book, name='adaugare'),
    path('useri/', views.cautare_user, name='useri'),
    path('show_user/<user_id>',views.show_user, name='show_user'),
    path('delete_utilizator/<user_id>',views.delete_utilizator, name='delete_utilizator'),
    path('dezactivate_utilizator/<user_id>',views.dezactivate_utilizator, name='dezactivate_utilizator'),
    path('inchiriere/<book_id>',views.show_carte, name='inchiriere'),
    path('inchiriat_carte/<book_id>',views.inchiriaza_carte, name='inchiriat_carte'),
    path('raportare/', views.raportare_carti, name='raportare'),


]
