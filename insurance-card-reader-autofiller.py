import cv2
import pytesseract
from selenium import webdriver
import pygetwindow as gw

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    cv2.imshow("Saftinet Insurance Card Scanner", img)
    key = cv2.waitKey(1)
    if key == ord("q") or key == 27: 
        break

def extract_data_from_qr_code():
    while True:
        _, img = cap.read()
        data = pytesseract.image_to_string(img)
        if data and data.count(",") == 10:
            print(data)
            return data
            

def fill_website_form(data):
    driver = webdriver.Chrome()  # You need to have the Chrome driver installed

    browser_window = None
    for window in gw.getAllTitles():
        if "Instagram" in window:
            browser_window = window
            break

    if browser_window:
        driver.switch_to.window(driver.window_handles[0])

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
    driver.find_element_by_id("OPM DED In Network").send_keys(opm_in_network)
    driver.find_element_by_id("OPM Out of Network").send_keys(opm_out_network)

    # Do not submit the form

    driver.quit()

if __name__ == "__main__":
    qr_data = extract_data_from_qr_code()
    fill_website_form(qr_data)
    cap.release()
    cv2.destroyAllWindows()
