"""prueba1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from prueba1.views import saludo, despedida, dame_fecha, calcula_edad, cursoC, cursoCss

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('nosveremos/', despedida),
    path('fecha/', dame_fecha),
    path('edades/<int:edad>/<int:anio>', calcula_edad),#se indica el parametro entre signo de mayor y menor 
    path('cursoC/', cursoC),
    path('cursoCss/', cursoCss)
]
