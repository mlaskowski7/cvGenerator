from django.urls import path
from . import views
urlpatterns = [
    path('',views.acceptView, name= 'acceptView'),
    path('cv/<int:id>/',views.cvView, name='cv'),
]
