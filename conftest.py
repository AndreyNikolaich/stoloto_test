import pytest
import json
import os.path
from fixture.application import Application


fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
    if target is None:
        with open(config_file) as config_file1:
            target = json.load(config_file1)
    if fixture is None or not fixture.is_valid():
        fixture = Application(base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture

@pytest.fixture(scope="function", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")




