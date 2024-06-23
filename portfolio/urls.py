from django.contrib import admin
from django.urls import path, include

from portfolio import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project-list'),
    path('create/', views.ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('project/<int:pk>/update', views.ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete', views.ProjectDeleteView.as_view(), name='project-delete'),

]