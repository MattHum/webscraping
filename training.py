import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get('https://edikte.justiz.gv.at/edikte/ex/exedi3.nsf/suche!OpenForm&subf=vex')
time.sleep(30) # Let the user actually see something!
#driver.quit()