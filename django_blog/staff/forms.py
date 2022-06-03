from django import forms
from blog.models import Category

class ReplyFeedbackForm(forms.Form):
    subject = forms.CharField(label="Subject", max_length=225)
    message = forms.CharField(widget=forms.Textarea)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # fields = '__all__'
        fields = ['name']    