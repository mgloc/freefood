"""
# Filename: run_selenium.py
"""
import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Selenium functions
def find_element_by_class_name(browser: webdriver.Chrome, class_name: str):
    return browser.find_element(By.XPATH, f"//div[@class='{class_name}']")


def find_elements_by_class_name(browser: webdriver.Chrome, class_name: str):
    return browser.find_elements(By.XPATH, f"//div[@class='{class_name}']")


def get_browser(headless: bool = True) -> webdriver.Chrome:
    ## Setup chrome options
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")

    # Set path to chromebrowser as per your configuration
    homedir = os.path.expanduser("~")
    driver_service = Service(
        f"{homedir}/chromedriver/chromedriver-linux64/chromedriver"
    )

    # Choose Chrome Browser
    web_browser = webdriver.Chrome(service=driver_service, options=chrome_options)
    web_browser.implicitly_wait(4)
    return web_browser


# Scraping functions


def remove_google_box(browser: webdriver.Chrome):
    original_window = browser.current_window_handle
    time.sleep(2)
    google_box = find_element_by_class_name(
        browser,
        class_name="fs-5 rounded-pill d-inline-block cursor-pointer text-uppercase fw-semi-bold px-4 py-2",
    )
    google_box.click()
    browser.switch_to.window(original_window)


def shuffle_cards(browser: webdriver.Chrome):
    shuffle_box = find_element_by_class_name(
        browser,
        class_name="fs-5 rounded-pill d-inline-block cursor-pointer text-uppercase fw-semi-bold px-4 py-2",
    )
    shuffle_box.click()


def pick_card(browser: webdriver.Chrome):
    card = find_element_by_class_name(
        browser,
        class_name="card",
    )
    card.click()
    return card


def get_prize_name(browser: webdriver.Chrome):
    prize_name = find_element_by_class_name(
        browser,
        class_name="fs-4 text-uppercase fw-semi-bold mb-3 lh-sm",
    ).text
    return prize_name.removeprefix("VOUS AVEZ GAGNÉ ")


def get_freefood(browser: webdriver.Chrome) -> str:
    """Browse on luckylikes.fr to get random free food from Burger King Cesson-Sévigné,
    stops when a prize is won and do not redeem it"""

    browser.get("https://app.luckylikes.fr/game/burgerkingcessonsevigne")

    remove_google_box(browser)
    shuffle_cards(browser)
    pick_card(browser)
    return get_prize_name(browser)


def add_prize_name_to_file(prize_name: str):
    with open("data/prizes.txt", "a", encoding="utf-8") as file:
        file.write(prize_name + "\n")


def fill_form(browser: webdriver.Chrome):
    # Fill form
    name = browser.find_element(
        By.ID,
        value="mat-input-0",
    )
    name.send_keys("John")

    mail = browser.find_element(
        By.ID,
        value="mat-input-1",
    )
    mail.send_keys("gajexab341@ipniel.com")

    mobile = browser.find_element(
        By.ID,
        value="mat-input-2",
    )
    mobile.send_keys("0606060606")

    checkbox = browser.find_element(
        By.ID,
        value="mat-mdc-checkbox-1-input",
    )
    checkbox.click()

    submit = find_element_by_class_name(
        browser,
        class_name="fs-5 rounded-pill d-inline-block cursor-pointer text-uppercase fw-semi-bold px-4 py-2",
    )
    submit.click()
    time.sleep(2)


def main():
    for _ in range(1000):
        browser = get_browser(headless=True)
        prize = get_freefood(browser)
        add_prize_name_to_file(prize)
        print(prize)
        if "CHEESEBURGER" in prize:
            fill_form(browser)
        browser.quit()


if __name__ == "__main__":
    main()
