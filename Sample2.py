from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def setup_module(module):
    global driver

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("http://www.fb.com/")
    driver.maximize_window()
    driver.implicitly_wait(30)


def tearDown_module(module):
    driver.close()


def test_verifyTittle():
    actual_title = driver.title

    assert actual_title == "Facebook – log in or sign up"


def test_verifyUrl():
    actual_url = driver.current_url
    assert actual_url == "https://www.facebook.com/"


def test_verifyHomepage_text():
    actual_text = driver.find_element(By.CLASS_NAME, "_8eso").text
    assert actual_text == "Facebook helps you connect and share with the people in your life."


def test_verifyUsername_textbox_enable():

    actual_utextbox=driver.find_element(By.ID,"email").is_enabled()

    assert  actual_utextbox == False


def test_verifyUsername_textbox_display():
    actual_utextbox = driver.find_element(By.ID, "email").is_displayed()
    assert actual_utextbox == True


def test_verifyUsername_textbox_typed_text():
    driver.find_element(By.ID, "email").send_keys("victor")
    actual_utextbox=driver.find_element(By.ID,"email").get_attribute("value")
    assert actual_utextbox == "victor"
