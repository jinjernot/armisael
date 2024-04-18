from selenium import webdriver

from config import user_etma, pass_etma, user_hp, pass_hp, etma_url, etma_inbox_url 
from app.click_checkbox import click_checkbox
from app.update_url import update_url
from app.login import login

driver = webdriver.Chrome() 

driver.get(etma_url)

# Funcion para logearse
login(driver, user_etma, pass_etma, user_hp, pass_hp)

# Funcion para cambiar url
update_url(driver, etma_inbox_url) # TDC a click

# Funcion para clickear el checkbox
click_checkbox(driver)

while True:
    pass