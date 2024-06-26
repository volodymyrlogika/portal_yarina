from django.contrib import admin
from django.urls import path, include

from forum import views

urlpatterns = [
    path('', views.TopicListView.as_view(), name='topic-list'),
    path('create/', views.TopicCreateView.as_view(), name='topic-create'),
    path('topic/<int:pk>', views.TopicDetailView.as_view(), name='topic-detail'),

]