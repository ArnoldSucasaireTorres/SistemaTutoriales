"""SistemaTutoriales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include,url
#clases propias

from SistemaTutoriales.views import index
from usuarios import views as vu

#Clases para el login
from . import views as vw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    #url(r'^foro/$', vu.foro),
    url(r'^pregunta/$',vu.pregunta),
    url(r'^comentario/$',vu.comentario),
    url(r'^calificacion/$',vu.calificacion),
    url(r'^aRespuesta/$',vu.aniadir_respuesta),
    url(r'^eRespuesta/$',vu.eliminar_respuesta),
    url(r'^reRespuesta/$',vu.editar_respuesta),
    path('foro/', vu.foro, name='foro'),
    #ruta para el registro, login y logout
    path('login', vw.login_user, name='login'),
    path('register', vw.register, name='register'),
    path('logout_user', vw.logout_user, name='logout_user'),
    #ruta del search
    path('search_e/', vu.search_e),
    #ruta para ver Historial
    path('verHistorial/<int:id>',vu.verHistorial,name='verHistorial'),
    path('editarPerfil/<int:id>',vu.editarPerfil,name='editarPerfil'),
    path('eliminarCuenta/<int:id>',vu.eliminarCuenta,name='eliminarCuenta'),
    path('editarPregunta/<int:id>',vu.editarPregunta,name='editarPregunta'),
    path('eliminarPregunta/<int:id>',vu.eliminarPregunta,name='eliminarPregunta'),
    path('formular_p/', vu.formular_p),
    path('Enviar_Pregunta/', vu.Enviar_Pregunta),
]