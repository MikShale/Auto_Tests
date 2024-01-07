import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"


try:
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    browser.switch_to.window(browser.window_handles[1])

    expression = browser.find_element(By.CSS_SELECTOR, '.form-group label span.nowrap').text
    expression = expression.split(' ')[2]
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    example = (expression.
               replace('x', str(x)).
               replace('sin', 'math.sin').
               replace('ln', 'math.log').
               replace('abs', 'math.fabs'))
    answer = float(eval(example)[0])

    browser.find_element(By.ID, 'answer').send_keys(answer)

    browser.find_element(By.CSS_SELECTOR, '[type = submit]').click()

    alert_text = browser.switch_to.alert.text.split(' ')[-1]

    print(alert_text)

    browser.quit()

finally:
    browser.quit()

