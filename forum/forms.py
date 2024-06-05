from django import forms

from forum.models import Topic


class TopicCreateForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super(TopicCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': "form-control mb-2"})

