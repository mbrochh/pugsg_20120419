"""Views for the ``guestbook`` app."""
from django.views.generic import ListView

from guestbook.models import GuestbookEntry


class GuestbookListView(ListView):
    model = GuestbookEntry
