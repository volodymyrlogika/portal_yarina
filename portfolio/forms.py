from django import forms

from portfolio.models import Project


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'text', 'image', 'file', 'link']

    def __init__(self, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': "form-control mb-2"})