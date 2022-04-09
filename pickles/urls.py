from django.urls import path

from . import views

app_name = 'pickles'
urlpatterns = [
    path('', views.pickles_all, name='index'),
    path('review/<int:review_id>', views.review, name='review'),
    path('review/new', views.review_new, name='new review'),
    path('<int:pickle_id>', views.pickle, name='pickle'),
    path('new', views.pickle_new, name='new pickle'),
    path('manufacturer', views.pickle_maker_new, name="new pickle maker"),
    path('manufacturer/<int:pickle_maker_id>', views.pickle_maker, name="pickle maker"),
    path('manufactuer/all', views.pickle_maker_all, name='all pickle makers'),
    path('tag/all', views.tags_all, name='all tags')
]