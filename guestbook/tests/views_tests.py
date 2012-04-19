"""Unittests for the views of the ``guestbook`` app."""
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory

from guestbook.views import GuestbookListView


class GuestbookListViewTestCase(TestCase):
    """Tests for the ``DashboardListView`` view class."""
    def test_adds_form_to_context(self):
        request = RequestFactory().get(reverse('guestbook_list'))
        view = GuestbookListView.as_view()
        resp = view(request)
        self.assertTrue('form' in resp.context_data)
