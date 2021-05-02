import pytest

# Test fixtures with parameters passed


def test_cross(setup, crossBrowser):
    # This cross browser will run from conftest.py
    print(crossBrowser)


def test_cross_two(setup, crossBrowserTwo):
    print(crossBrowserTwo)
