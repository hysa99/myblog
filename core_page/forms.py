from django import forms
from .models import BlogItems, Subscriber



INPUT_CLASSES = "w-full py-4 px-6 rounded-2xl border"



class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogItems
        fields = ('category', 'title', 'description', 'images')
        title = forms.CharField()
        description = forms.Textarea()
        images = forms.FileInput()


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['full_name', 'email']
        full_name = forms.CharField()
        email = forms.EmailField()

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            return instance



