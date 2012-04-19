"""Some useful Fabric tasks."""
from fabric.api import local


def flake8():
    """Checks PEP8 compliancy for all files in the project."""
    local('flake8 --statistics .')


def test(all=1):
    """Runs the test suite."""
    cmd = './manage.py test --settings=pugsg20120419.test_settings guestbook'
    if all == 1:
        cmd += ' integration_tests'
    local(cmd)
