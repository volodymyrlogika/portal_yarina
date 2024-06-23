from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from portfolio import models
from portfolio.forms import ProjectCreateForm


class ProjectListView(LoginRequiredMixin, ListView):
    model = models.Project
    context_object_name = "projects"
    template_name = "portfolio/project_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = models.Project
    template_name = "portfolio/project_create.html"
    success_url = reverse_lazy('project-list')
    form_class = ProjectCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = models.Project
    template_name = "portfolio/project_detail.html"
    context_object_name = "project"


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Project
    template_name = "portfolio/project_update.html"
    success_url = reverse_lazy('project-list')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Project
    template_name = "portfolio/project_delete.html"
    success_url = reverse_lazy('project-list')
