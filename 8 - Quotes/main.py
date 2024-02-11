from selenium import webdriver
from selenium.webdriver.common.by import By


def sepTags(string):
    li = list(string.split(" "))
    return li


def login(user, key):
    driver.find_element(By.XPATH, '//a[contains(@href,"login")]').click()

    username = driver.find_element(By.CSS_SELECTOR, "#username")
    username.send_keys(user)

    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys(key)

    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


driver = webdriver.Firefox()
driver.get("https://quotes.toscrape.com/")


login("Scraper", "teste")

quotes_tag = driver.find_elements(By.CSS_SELECTOR, ".quote")

for info in quotes_tag:
    quote = info.find_element(By.CSS_SELECTOR, ".text").text
    author = info.find_element(By.CSS_SELECTOR, ".author").text
    tags = info.find_element(By.CSS_SELECTOR, ".tags").text[6:]
    tags = sepTags(tags)
    print(f"{author}: {quote}\n{tags}")

driver.quit()
