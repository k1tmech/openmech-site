from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pages-home'),
    path('dashboard/', views.dashboard, name='pages-dashboard'),
    #path('blogs/', views.blogs, name='pages-blogs'),
    #path('forum/', views.forum, name='pages-forum'),
    #path('groups/', views.groups, name='pages-group'),
    path('learn/', views.learn, name='pages-learn'),
    #path('mechlab/', views.mechlab, name='pages-mechlab'),
    #path('ecosystem/', views.ecosystem, name='pages-ecosystem'),
    #path('members/', views.members, name='pages-members'),
]