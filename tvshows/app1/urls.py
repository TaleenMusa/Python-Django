from django.urls import path
from . import views
urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.addshow),
    path('submitshow', views.submitshow),
    path('shows/<id>', views.display),
    path('shows/<id>/edit', views.edit),
    path('shows/<id>/update', views.update),
    path('delete/<id>', views.delete),
]
