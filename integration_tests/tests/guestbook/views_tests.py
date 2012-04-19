"""Integration tests for the view of the ``guestbook`` app."""
from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase, TestCase

from selenium.webdriver.firefox.webdriver import WebDriver


class GuestbookListViewTestCase(TestCase):
    def test_is_callable(self):
        resp = self.client.get(reverse('guestbook_list'))
        self.assertEqual(resp.status_code, 200)


class GuestbookListViewSeleniumTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(GuestbookListViewSeleniumTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(GuestbookListViewSeleniumTestCase, cls).tearDownClass()
        cls.selenium.quit()

    def test_renders_the_form(self):
        self.selenium.get('%s%s' % (self.live_server_url,
            reverse('guestbook_list')))
        self.selenium.find_element_by_tag_name('form')
