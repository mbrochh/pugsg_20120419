"""Forms of the ``guestbook`` app."""
from django import forms

from guestbook.models import GuestbookEntry


class GuestbookEntryForm(forms.ModelForm):
    class Meta:
        model = GuestbookEntry
