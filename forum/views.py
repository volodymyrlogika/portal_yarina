from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from forum import models
from forum.forms import TopicCreateForm, MessageForm


class TopicListView(LoginRequiredMixin, ListView):
    model = models.Topic
    context_object_name = "topics"
    template_name = "topics/topic_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = models.Topic
    template_name = "forum/topic_create.html"
    success_url = reverse_lazy('topic-list')
    form_class = TopicCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TopicUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Topic
    template_name = "forum/topic_update.html"
    success_url = reverse_lazy('topic-list')


class TopicDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Topic
    template_name = "forum/delete_topic.html"
    success_url = reverse_lazy('task-list')


class TopicDetailView(LoginRequiredMixin, DetailView):
    model = models.Topic
    template_name = "forum/topic_detail.html"
    context_object_name = "topic"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['message_form'] = MessageForm()
        return context

    def post(self, request, *args, **kwargs):
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.author = self.request.user
            message.topic = self.get_object()
            message.save()

        return redirect('topic-detail', pk=self.get_object().pk)