from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('review/<int:review_id>', views.review, name='review'),
    path('review/new', views.review_new, name='new review'),
    path('<int:pickle_id>', views.pickle, name='pickle'),
    path('new', views.pickle_new, name='new pickle')
]