from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def click_element(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    except ElementClickInterceptedException:
        print("Element click intercepted, trying JavaScript click.")
        driver.execute_script("arguments[0].click();", element)
    except TimeoutException:
        print(f"Timeout: Element {value} not found.")

def fill_form():
    driver = webdriver.Edge()
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdKIfQwSt3Dde8noWvJpkI8SyINCQgOPpuHqwrnjVCAeYt3wg/viewform")
    challenge = "Customer/Consumer"
    
    click_element(driver, By.XPATH, f"//div[@data-value='{challenge}']")
    
    driver.quit()

if __name__ == "__main__":
    fill_form()
