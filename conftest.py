import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(7)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        browser.implicitly_wait(7)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()


"""
1) # Added DriverManager (autocheck/autodownload driver)
# browser = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

2) # If you need to run tests with Firefox browser (install before)
pytest -s -v --browser_name=firefox test_1.py

3) # To rerun tests
pip install pytest-rerunfailures (added)
pytest -v --tb=line --reruns 1 --browser_name=chrome test_1.py

"""