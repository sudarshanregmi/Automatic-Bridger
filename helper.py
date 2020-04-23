from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

import common


driver = webdriver.Chrome()
driver.get(common.url)
driver.implicitly_wait(3)


def select_frame(frame):
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, frame))) 


def select_id_from_frame(frame, idx):
    select_frame(frame)
    driver.find_element_by_id(idx).click()
    driver.switch_to.parent_frame()


def restart():
    select_id_from_frame("bottomLeftFrame", "a43")
    select_frame("bottomLeftFrame")
    driver.find_element_by_id("a49").click()
    driver.switch_to.parent_frame()
    select_frame("mainFrame")
    driver.find_element_by_id("reboot").click()
    driver.switch_to.alert.accept()

