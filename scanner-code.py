import cv2
import pytesseract
from selenium import webdriver
from pygetwindow import getWindowsWithTitle
import pyautogui

cap = cv2.VideoCapture(0)
while True:
    cv2.imshow("Saftinet Insurance Card Scanner")
    key = cv2.waitKey(1)
    if cv2.waitKey(1) == ord("q") or key == 27:
        break


def extract_data_from_qr_code():
    while True:
        _, img = cap.read()
        data = pytesseract.image_to_string(img)
        if data and data.count(",") == 10:
            return data

def fill_website_form(data, tab_title):
    driver = webdriver.Chrome()  # Download Chrome driver installed
    driver.get("https://www.google.com") 

    found_tab = None
    for window in getWindowsWithTitle(tab_title):
        if window.title == tab_title:
            found_tab = window
            break

    if found_tab:
        found_tab.activate()


    # Split the data into fields
    fields = data.split(',')
    
    name, id_number, group_no, rxbin, rxpcn, rxgrp, plan_code, ded_in_network, ded_out_network, opm_in_network, opm_out_network = fields

    driver.find_element_by_id("Name").send_keys(name)
    driver.find_element_by_id("ID").send_keys(id_number)
    driver.find_element_by_id("Group").send_keys(group_no)
    driver.find_element_by_id("RXBIN").send_keys(rxbin)
    driver.find_element_by_id("RXPCN").send_keys(rxpcn)
    driver.find_element_by_id("RXGRP").send_keys(rxgrp)
    driver.find_element_by_id("Plan").send_keys(plan_code)
    driver.find_element_by_id("DED In Network").send_keys(ded_in_network)
    driver.find_element_by_id("DED Out of Network").send_keys(ded_out_network)
    driver.find_element_by_id("OPM In Network").send_keys(opm_in_network)
    driver.find_element_by_id("OPM Out of Network").send_keys(opm_out_network)

    driver.quit()

if __name__ == "__main__":
    
    qr_data = extract_data_from_qr_code()
    active_tab_title = "Google - Google Chrome"  # Replace with the actual title of the tab you want to interact with
    fill_website_form(qr_data, active_tab_title)
    cap.release()
    cv2.destroyAllWindows()
