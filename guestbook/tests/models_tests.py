"""Tests for the models of the ``guestbook`` app."""
from django.test import TestCase

from guestbook.models import GuestbookEntry


class GuestbookEntryTestCase(TestCase):
    """Tests for the ``GuestbookEntry`` model class."""
    def test_instantiation_and_save(self):
        entry = GuestbookEntry(author='user@example.com', text='hello world')
        entry.save()
        self.assertTrue(entry.pk, msg=(
            'New object should have a primary key.'))

    def test_character_count(self):
        entry = GuestbookEntry(author='user@example.com', text='hello world')
        self.assertEqual(entry.character_count(), 11)
