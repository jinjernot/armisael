from selenium import webdriver

from app.login import login
from app.click_element import click_on_element
from config import username, password

website_url = "https://hp-tmsweb-itg.inc.hp.com/"
element_id = "projects"

driver = webdriver.Chrome()

driver.get(website_url)

login(driver, username, password)
 
click_on_element(driver, element_id)
