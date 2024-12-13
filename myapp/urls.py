from django.urls import path
from . import views
urlpatterns = [
    path('',views.hello), #llamo a las views y la funcion llamada hello
    path("miguel/",views.about)
]
