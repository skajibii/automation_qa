from selenium.webdriver.common.by import By


class TexBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName'")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail'")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress'")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress'")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit'")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.XPATH, '//button[@title="Expand all"]')
    TITLE_LIST = (By.XPATH, '//span[@class="rct-title"]')
    CHECK_BOX_LIST = (By.XPATH, '//span[@class="rct-checkbox"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')
    TITLE_LIST_TEXT = './/ancestor::span[@class="rct-text"]'
