"""Models for the ``guestbook`` app."""
from django.db import models


class GuestbookEntry(models.Model):
    author = models.EmailField()
    text = models.TextField()

    def character_count(self):
        return len(self.text)
