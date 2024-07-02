import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    else:
        driver = webdriver.Ie()
        print("Launching Internet Explorer browser")
    yield driver
    driver.quit()


# Add command line option for selecting browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


# Hooks for adding environment info to HTML reports
def pytest_configure(config):
    config._metadata = {'Project Name': 'nop Commerce', 'Module Name': 'Customers',
                        'Tester': 'Priyal'}  # Initialize metadata if it does not exist


# Hooks to delete/modify environment info in HTML reports
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
    metadata.pop("Plugins", None)
