from django.urls import path

from . import views

app_name = 'dreamcatcher'

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('rating', views.rating, name='rating'),
    path('login_view', views.login_view, name='login_view'),
    path('login_register_view', views.login_register_view, name='login_register_view'),
    path('login_register', views.login_register, name='login_register'),
    path('descriere_categorie', views.descriere_categorie, name='descriere_categorie'),
    path('statistici', views.statistici_view, name='statistici_view'),
    path('statistici_stres', views.statistici_view_stres, name='statistici_view_stres'),
    path('statistici_energie', views.statistici_view_energie, name='statistici_view_energie'),
    path('statistici_durata', views.statistici_view_durata, name='statistici_view_durata'),
    path('back', views.back_to_statistici_view, name='back_to_statistici_view'),

]