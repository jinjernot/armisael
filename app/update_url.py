import time

def update_url(driver, new_url):
    driver.get(new_url)
    
    time.sleep(5) # tiempo para que cargue la url