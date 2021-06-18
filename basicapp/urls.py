from django.urls import path, include
from basicapp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('addpeeevent', views.addpee, name='addpee'),
    path('addpoopevent', views.addpoop, name='addpoop'),
    path('addwalkevent', views.addwalk, name='addwalk'),
    path('addeatevent', views.addeat, name='addeat'),
    path('addmedicineevent', views.addmedicine, name='addmedicine'),
    path('addnothingevent', views.addnothing, name='addnothing'),
]