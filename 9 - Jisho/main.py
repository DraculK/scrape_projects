from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://jisho.org/")

search = driver.find_element(By.CSS_SELECTOR, "#keyword")
word = input("Write a word in english: ")
search.send_keys(word)
driver.find_element(By.CSS_SELECTOR, ".submit").click()
kanjis = driver.find_elements(By.CSS_SELECTOR, "span.text")

print("Possible answers: ")
for ele in kanjis[1:]:
    print(ele.text)
driver.quit()
