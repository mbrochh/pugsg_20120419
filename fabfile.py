"""Some useful Fabric tasks."""
from fabric.api import local


TEST_APPS = [
    'guestbook',
]

TEST_COMMAND = ('./manage.py test --settings=pugsg20120419.test_settings %s' %
    ' '.join(TEST_APPS))


def coverage(all='1', html='1'):
    """Runs the test suite."""
    cmd = 'coverage run --source=%s %s' % (','.join(TEST_APPS), TEST_COMMAND)
    if all == '1':
        cmd += ' integration_tests'
    local(cmd)
    if html == '1':
        local('coverage html')
        local('xdg-open htmlcov/index.html')


def flake8():
    """Checks PEP8 compliancy for all files in the project."""
    local('flake8 --statistics .')


def test(all='1'):
    """Runs the test suite."""
    cmd = TEST_COMMAND
    if all == '1':
        cmd += ' integration_tests'
    local(cmd)
