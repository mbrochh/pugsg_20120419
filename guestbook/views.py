"""Views for the ``guestbook`` app."""
from django.views.generic import ListView

from guestbook.models import GuestbookEntry
from guestbook.forms import GuestbookEntryForm


class GuestbookListView(ListView):
    model = GuestbookEntry

    def get_context_data(self, **kwargs):
        context = super(GuestbookListView, self).get_context_data(**kwargs)
        context.update({
            'form': GuestbookEntryForm(),
        })
        return context
