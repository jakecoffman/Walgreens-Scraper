import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def watch_zip_code(zip_code):
    driver = webdriver.Chrome()
    driver.get("https://www.walgreens.com/findcare/vaccination/covid-19")
    btn = driver.find_element_by_css_selector('span.btn.btn__blue')

    action = webdriver.ActionChains(driver)
    action.move_to_element(btn)
    action.click()
    action.perform()

    element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, "inputLocation"))
    )
    element.clear()
    element.send_keys(zip_code)
    button = driver.find_element_by_css_selector("button.btn")

    while True:
        button.click()
        alert_element = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p.fs16"))
        )
        if alert_element.text == "Appointments available!":
            print("APPOINTMENT FOUND! ZIP CODE: ", zip_code)
            return

        time.sleep(5)


if __name__ == "__main__":
    watch_zip_code(63119)
