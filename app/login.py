from selenium.webdriver.common.by import By
import time

def login(driver, user_etma, pass_etma, user_hp, pass_hp):
    hp_username_field = driver.find_element(By.ID, "username")
    hp_password_field = driver.find_element(By.ID, "password")

    hp_username_field.send_keys(user_hp)
    hp_password_field.send_keys(pass_hp)

    login_button = driver.find_element(By.XPATH, "//input[@value='Log on']")
    login_button.click()

    time.sleep(20)
    
    etma_username_field = driver.find_element(By.ID, "username")
    etma_password_field = driver.find_element(By.ID, "password")

    etma_username_field.send_keys(user_etma)
    etma_password_field.send_keys(pass_etma)


    login_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    login_button.click()
    time.sleep(10)