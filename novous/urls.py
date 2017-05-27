from django.conf.urls import url, include

# from novousapp import admin
from django.contrib import admin
from novousapp import views

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    # url(r'^fuel/',include('novousapp.urls')),
    url(r'^fuelrest/',views.FuelStationList.as_view()),
    url(r'^options/',views.options),
    url(r'^searchpage/',views.searchpage),
    ]