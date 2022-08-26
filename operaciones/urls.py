from django.urls import path

from . import views

urlpatterns = [
    # ex: localhost:8000/operaciones/sumar/n1/n2/
    path('sumar/<int:n1>/<int:n2>/', views.suma, name='suma'),
    # ex: localhost:8000/operaciones/restar/n1/n2/
    path('restar/<int:n1>/<int:n2>/', views.resta, name='resta'),
    # ex: localhost:8000/operaciones/multiplicar/n1/n2/
    path('multiplicar/<int:n1>/<int:n2>/', views.multiplicacion, name='multiplicacion'),
]
