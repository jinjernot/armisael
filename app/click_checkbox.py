from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_checkbox(driver):
    driver.switch_to.frame("content") # se mueve al iframe content

    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "inboxSelectAll")) # selecciona el checkbox
    )
    checkbox.click()

    take_ownsership = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "own")) # selecciona el checkbox
    )
    take_ownsership.click()

    take_ownsership_yes = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "own_yes")) # selecciona el checkbox
    )
    take_ownsership_yes.click()

    