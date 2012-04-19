"""Tests for the forms of the ``guestbook`` app."""
from django.test import TestCase

from guestbook.forms import GuestbookEntryForm


class GuestbookEntryFormTestCase(TestCase):
    """Tests for the ``GuestbookEntryForm`` model form."""
    def test_fields_are_mandatory(self):
        form = GuestbookEntryForm(data={})
        self.assertFalse(form.is_valid(), msg=(
            'The form should be invalid when no data given.'))
        self.assertTrue('author' in form.errors, msg=(
            'The author field should be mandatory.'))
        self.assertTrue('text' in form.errors, msg=(
            'The text field should be mandatory.'))
