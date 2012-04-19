"""Integration tests for the view of the ``guestbook`` app."""
from django.core.urlresolvers import reverse
from django.test import TestCase


class GuestbookListViewTestCase(TestCase):
    def test_is_callable(self):
        resp = self.client.get(reverse('guestbook_list'))
        self.assertEqual(resp.status_code, 200)
