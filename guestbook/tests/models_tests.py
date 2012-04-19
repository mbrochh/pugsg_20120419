"""Tests for the models of the ``guestbook`` app."""
from django.test import TestCase

from guestbook.tests.factories import GuestbookFactory


class GuestbookEntryTestCase(TestCase):
    """Tests for the ``GuestbookEntry`` model class."""
    def test_instantiation_and_save(self):
        entry = GuestbookFactory.build()
        entry.save()
        self.assertTrue(entry.pk, msg=(
            'New object should have a primary key.'))

    def test_character_count(self):
        entry = GuestbookFactory.build(text='Hello world')
        self.assertEqual(entry.character_count(), 11)
