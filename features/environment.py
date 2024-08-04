from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from utilities import ConfigReader


def before_scenario(context, driver):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic_info", "url"))


def after_scenario(context, driver):
    context.driver.quit()
