from django import forms

class ReplyFeedbackForm(forms.Form):
    subject = forms.CharField(label="Subject", max_length=225)
    message = forms.CharField(widget=forms.Textarea)