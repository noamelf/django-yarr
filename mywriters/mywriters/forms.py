from django import forms

class AddFeedForm(forms.ModelForm):
    required_css_class = "required"

    class Meta:
        model = models.Feed
        fields = ["feed_url"]
        widgets = {"feed_url": forms.TextInput()}

