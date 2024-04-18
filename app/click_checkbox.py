from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_checkbox(driver):
    driver.switch_to.frame("content")

    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "inboxSelectAll"))
    )
    checkbox.click()