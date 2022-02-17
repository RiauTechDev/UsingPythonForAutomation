from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url = 'https://waves.tech'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 15)

startBuildingButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/tui-root/tui-portal-host/div[2]/ui-common-layout/div/section/app-main-page/div/main-intro/div/div/div[1]/ui-slide-up-animation[2]/a/tui-wrapper')))
startBuildingButton.click()