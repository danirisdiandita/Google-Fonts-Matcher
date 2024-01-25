from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 
# Replace 'path/to/chromedriver' with the path to your chromedriver executable
driver = webdriver.Chrome()

# Open a website
driver.get('https://fonts.google.com/')

# Find an element by its name and interact with it
SCROLL_PAUSE_TIME = 3


fontset = set([])
# Get scroll height
current_height = 0 

increment = 800
firstline = True  
while True:
    # Scroll down to bottom
    driver.execute_script(f"window.scrollTo({current_height}, {current_height+increment})")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)



    elements = driver.find_elements(By.CLASS_NAME, 'gf-block-anchor')
    for el in elements: 
        font_ = el.get_attribute('href')
        if font_ not in fontset: 
            with open('fontLink.txt', 'a') as f: 
                if firstline: 
                    f.write(font_)
                    firstline = False 
                else: 
                    f.write('\n' + font_)
        fontset.add(font_)
    current_height += increment
# element.send_keys('Selenium WebDriver')

# Click on a button


# Wait for a few seconds
driver.implicitly_wait(5)

# Close the browser window
driver.quit()
