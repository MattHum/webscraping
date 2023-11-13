import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
driver = webdriver.Chrome()

#tips
#element = driver.find_element(By.ID, "passwd-id")
#element = driver.find_element(By.NAME, "passwd")
#element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
#element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")

#edikte
# Bundeslandauswahl -> dev 'col-sm-9' /select name "BL, tabindex ="19
# PLZ -> dev 'col-sm-9' / input name "VPLZ" value tabindex="18"
# Suchfunktion -> class="col-sm-9 col-sm-offset-3" /name "sebut" class "btn btn-primary"

# hier weiter lesen: https://selenium-python.readthedocs.io/navigating.html


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)
driver.get("https://edikte.justiz.gv.at/edikte/ex/exedi3.nsf/suche!OpenForm&subf=vex")

h1 = driver.find_element(By.NAME, "VPLZ")
h1.send_keys("1140")

# Assume the button has the ID "submit" :)
driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()

driver.implicitly_wait(5)


time.sleep(30) # Let the user actually see something!
#driver.quit()

#print(driver.page_source)
driver.quit()