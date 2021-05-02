import pytest


@pytest.fixture()
def setup():
    print("Start Setup")
    yield
    print("Stop Setup")


# parameterizing tests with multiple datasets using fixtures
@pytest.fixture(params=["chrome", "firefox", "edge"])
def crossBrowser(request):
    """ --> as it will run 3 times but if you want to pass some varible to chrome then follow chromeBrowserTwo method
    --> this request is attach to param variable which will take each value from params list """
    return request.param


@pytest.fixture(params=[("chrome", "Rohit", "Tupe"), ("firefox", "omkar"), "edge"])
def crossBrowserTwo(request):
    return request.param
