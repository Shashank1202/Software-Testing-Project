from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

# Initialize Chrome WebDriver (replace with Firefox WebDriver if needed)
chromedriver_path = "./chromedriver.exe"  # Adjust for your path
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

def highlight_element(element):
    driver.execute_script("arguments[0].setAttribute('style', 'border: 6px solid red;');", element)
    time.sleep(5)
    driver.execute_script("arguments[0].setAttribute('style', 'border: 0px;');", element)

# Open Amazon.in
driver.get("your_website_name")
driver.maximize_window()
time.sleep(5)

person= driver.find_element(By.XPATH, "//*[@id='user-menu']/div")
highlight_element(person)
person.click()
time.sleep(5)

email = driver.find_element(By.XPATH, "//*[@id='email']")
highlight_element(email)
email.send_keys("your_login_email")
time.sleep(5)

pwd = driver.find_element(By.XPATH, "//*[@id='passwd']")
highlight_element(pwd)
pwd.send_keys("Password")
time.sleep(5)

proceed = driver.find_element(By.XPATH, "//*[@id='row-submit']/div/button")
highlight_element(proceed)
proceed.click()
time.sleep(5)

rakhi = driver.find_element(By.XPATH, "//*[@id='selection-panel']/div[2]/a[1]")
highlight_element(rakhi)
rakhi.click()
time.sleep(5)

#kids = driver.find_element(By.XPATH, "//*[@id='selection-panel']/div[2]/a[4]")
#highlight_element(kids)
#kids.click()
# wtime.sleep(5)



gift = driver.find_element(By.XPATH, "//*[@id='product-grid']/div[1]/div/a/img")
highlight_element(gift)
gift.click()
time.sleep(5)

add = driver.find_element(By.XPATH, "//*[@id='add-cart']")
highlight_element(add)
add.click()
time.sleep(5)


pin = driver.find_element(By.XPATH, "//*[@id='location-input']")
highlight_element(pin)
pin.send_keys("560056")
pin.click()
time.sleep(10)

date = driver.find_element(By.XPATH, "//*[@id='std-datepicker']")
highlight_element(date)
driver.execute_script("arguments[0].value = '2024-07-23';", date)
driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", date)
time.sleep(5)

add = driver.find_element(By.XPATH, "//*[@id='add-cart']")
highlight_element(add)
add.click()
time.sleep(5)


con = driver.find_element(By.XPATH, "//*[@id='add-cart']")
highlight_element(con)
con.click()
time.sleep(5)

con = driver.find_element(By.XPATH, "//*[@id='inc-quantity-650108']/img")
highlight_element(con)
con.click()
time.sleep(5)

con = driver.find_element(By.XPATH, "//*[@id='enabled-button']/a")
highlight_element(con)
con.click()
time.sleep(5)



name = driver.find_element(By.XPATH, "//*[@id='c-add-add-flow']/div[1]/div[2]/div[1]/div[2]/")
highlight_element(name)
name.send_keys("shashank")
name.click()
time.sleep(5)

con = driver.find_element(By.XPATH, "//*[@id='countName']")
highlight_element(con)
con.send_keys("India")
con.click()
time.sleep(5)

add = driver.find_element(By.XPATH, "//*[@id='c-add-add-flow']/div[1]/div[2]/div[4]/")
highlight_element(add)
add.send_keys("Bengaluru")
add.click()
time.sleep(5)

pin = driver.find_element(By.XPATH, "//*[@id='c-add-add-flow']/div[1]/div[2]/div[6]/div[1]/div[2]/div[3]/")
highlight_element(pin)
pin.send_keys("")
pin.click()
time.sleep(5)


