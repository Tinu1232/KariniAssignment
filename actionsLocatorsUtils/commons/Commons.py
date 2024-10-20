import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class Commons:

    def __init__(self, driver):
        self.driver = driver

    def waitForVisibility(self, xpath):
        wait = WebDriverWait(self.driver, 15)
        return  wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def pause(self, waitTill):
        return time.sleep(waitTill)

    def zoomOut(self, driver, percentage):
        return driver.execute_script(f"document.body.style.zoom='{percentage}';")

    def launchURL(self, url):
        self.driver.get(url)