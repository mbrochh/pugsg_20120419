from django.conf.urls import patterns, url

from guestbook.views import GuestbookListView


urlpatterns = patterns('',
    url(r'^$', GuestbookListView.as_view(), name='guestbook_list'),
)
