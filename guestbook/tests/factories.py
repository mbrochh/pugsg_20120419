"""Factories for models of the ``guestbook`` app."""
import factory

from guestbook.models import GuestbookEntry


class GuestbookFactory(factory.Factory):
    """Factory for the ``GuestbookEntry`` model."""
    FACTORY_FOR = GuestbookEntry

    author = 'user@example.com'
    text = 'Hello world!'
