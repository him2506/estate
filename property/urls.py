from django.urls import path

from .import views
urlpatterns = [
    path('', views.home ,name = 'home'),
    path('about',views.about,name = 'about'),
    path('properties',views.property,name='properties'),
    path('properties<int:prop_id>', views.single_prop, name='single_prop'),
    path('location<int:loc_id>',views.loc_prop, name = 'loc_prop')
]