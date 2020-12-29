from mywriters.models import UserFeeds
from django import forms



class AddFeedForm(forms.ModelForm):
    class Meta:
        model = UserFeeds
        fields = ["feeds"]
