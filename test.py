from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#edikte
# Bundeslandauswahl -> dev 'col-sm-9'
# Suchfunktion -> 

# hier weiter lesen: https://selenium-python.readthedocs.io/navigating.html


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)
driver.get("https://edikte.justiz.gv.at/edikte/ex/exedi3.nsf/suche!OpenForm&subf=vex")

h1 = driver.find_element(By.CLASS_NAME, 'col-sm-9')

print(driver.page_source)
driver.quit()