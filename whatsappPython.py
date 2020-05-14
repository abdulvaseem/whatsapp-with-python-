""" K ABDUL VASEEM AKRAM """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(r'D:\New folder\Abdul\chromedriver.exe')
driver.get(r"https://web.whatsapp.com/")
string title = "Hanish"
driver.findElement(By.CSS_SELECTOR("[title^='"+title+"']")).click();

inp_xpath = '[@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located(( 
    By.XPATH, inp_xpath)))
for i in range(50): 
    input_box.send_keys(string + Keys.ENTER) 
    time.sleep(5)
