from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from portfolio import models
from portfolio.forms import ProjectCreateForm
from portfolio.mixins import UserIsOwnerMixin


class AllProjectListView(LoginRequiredMixin, ListView):
    model = models.Project
    context_object_name = "projects"
    template_name = "portfolio/all_project_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class MyPortfolioView(LoginRequiredMixin, ListView):
    model = models.Project
    context_object_name = "projects"
    template_name = "portfolio/project_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author = self.request.user)
        return queryset

    
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


class ProjectUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = models.Project
    template_name = "portfolio/project_update.html"
    success_url = reverse_lazy('project-list')
    form_class = ProjectCreateForm


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Project
    template_name = "portfolio/project_delete.html"
    success_url = reverse_lazy('project-list')


def custom_403_view(request, exception=None):
    return render(request, "403.html", context={"message": "Немає доступу"}, status=403)
