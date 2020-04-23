#!/usr/local/bin/python3.6

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import argparse

from config import credentials as cred
from helper import select_frame, select_id_from_frame, driver


def main():
    select_id_from_frame("bottomLeftFrame", "a13")
    select_frame("mainFrame")
    # Disable dhcp
    driver.find_elements_by_css_selector("input[type='radio'][value='0']")[0].click()
    driver.find_elements_by_css_selector("input[type='submit'][value='Save']")[0].click()
    driver.switch_to.parent_frame()

    # Wireless settings
    select_id_from_frame("bottomLeftFrame", "a7")
    select_frame("mainFrame")
    driver.find_element_by_id("t_11n_only").click()
    driver.find_element_by_id("t_auto").click()

    driver.execute_script("document.getElementById('wdsbrl').checked = true")
    driver.find_elements_by_css_selector("input[id='survey']")[0].click()
    source_wifi_str = f"//*[contains(text(), '{cred['SOURCE_WIFI']}')]/parent::tr/td/a[@id='t_conn']"
    assert len(driver.find_elements_by_xpath(source_wifi_str)) == 1
    driver.find_elements_by_xpath(source_wifi_str)[0].click()
    driver.find_element_by_id("t_wpa").click()
    driver.find_element_by_id('keytext').clear()
    driver.find_element_by_id('keytext').send_keys(cred['SOURCE_WIFI_PASS'])
    driver.find_elements_by_css_selector("input[type='submit'][value='Save']")[0].click()
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    driver.switch_to.parent_frame()


    select_id_from_frame("bottomLeftFrame", "a9")
    select_frame("mainFrame")
    # Select security type and fill password
    driver.find_elements_by_css_selector("input[type='radio'][value='3']")[0].click()
    driver.find_element_by_id("pskSecret").clear()
    driver.find_element_by_id("pskSecret").send_keys(cred['BRIDGE_PASS']) 
    driver.find_elements_by_css_selector("input[type='submit'][value='Save']")[0].click()
    try:
        driver.switch_to.alert.dismiss()
    except:
        pass
    driver.switch_to.parent_frame()


    select_id_from_frame("bottomLeftFrame", "a3")
    select_frame("bottomLeftFrame")
    driver.find_element_by_id("a6").click()
    driver.switch_to.parent_frame()
    select_frame("mainFrame")

    # LAN IP address
    driver.execute_script(f"document.getElementById('lanip').value = '{cred['IP_ADDR']}'") 
    # driver.find_element_by_id('lanip').clear()
    # driver.find_element_by_id('lanip').send_keys('192.168.1.1')
    driver.find_elements_by_css_selector("input[type='submit'][value='Save']")[0].click()

    try:
        driver.switch_to.alert.accept()
    except :
        pass

    sleep(5)
    driver.close()


if __name__=='__main__':
    main()
