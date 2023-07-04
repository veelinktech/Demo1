from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def setup_module():
    global driver

    s = Service(executable_path="D:\\SeleniumDrivers\\chromedriver_win32_latest\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(30)


def teardown_module():
    driver.close()


def test_verifyTitle():
    actual_title = driver.title
    assert actual_title == "OrangeHRM"

def test_verifyUrl():
    actual_url = driver.current_url
    assert actual_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


def test_verifyLoginText():
    actual_text = driver.find_element(By.XPATH, "//h5[text()='Login']").text
    assert actual_text == "Login"

def test_m1():
    assert 5==5


def test_m2():
    assert 5>=2

def test_m3():
    assert 10+5==15


