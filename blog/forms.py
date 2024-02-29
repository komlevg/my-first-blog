from django import forms
from .models import SkyNews, Tag

class AddPostForm(forms.ModelForm):
    newscontent = forms.CharField(widget=forms.Textarea(), required=False,  label='контент новости')#required - если false - можно будет не заполнять

    class Meta:
        model = SkyNews
        fields = '__all__'
        # fields = ['title', 'slug']