from selenium.webdriver.common.by import By

def login(driver, username, password):
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button = driver.find_element(By.XPATH, "//input[@value='Log on']")
    login_button.click()