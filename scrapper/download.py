from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

options = webdriver.ChromeOptions()
prefs = {'download.default_directory': '/home/dani/Downloads/googlefonts'}
options.add_experimental_option('prefs', prefs)
# Replace 'path/to/chromedriver' with the path to your chromedriver executable
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# Open a website
# driver.get('https://fonts.google.com/specimen/Roboto')


# class_nutupi = '.gmat-subhead-2.callout__link'
# try: 
#     time.sleep(5)
#     class_nutupi_el = driver.find_element(By.CSS_SELECTOR, class_nutupi)
#     class_nutupi_el.click()
# except:
#     print('nutupi ilang')


class_to_click=".mdc-button.mdc-button--unelevated.mat-mdc-unelevated-button.rounded.fab-tablet-mobile-button.mat-primary.mat-mdc-button-base.gmat-mdc-button.ng-star-inserted"
fonts = []
with open('fontLink.txt') as f: 
    fonts = f.read().splitlines()

for fontpage in fonts: 
    driver.get(fontpage)
    class_nutupi = '.gmat-subhead-2.callout__link'
    try: 
        time.sleep(5)
        class_nutupi_el = driver.find_element(By.CSS_SELECTOR, class_nutupi)
        class_nutupi_el.click()
    except:
        print('nutupi ilang')

    download_button = driver.find_element(By.CSS_SELECTOR, class_to_click)
    download_button.click() 


# Wait for a few seconds
    time.sleep(10)


# Close the browser window
driver.quit()
